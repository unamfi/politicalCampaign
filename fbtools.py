# vim: set fileencoding=utf-8 fileformat=unix :

import facebook
import logging.config
import time

from iso8601 import parse_date
from sqlalchemy.orm import sessionmaker

from models import *
from utils import subdict
from common import _call_and_retry


TIME_AMOUNT = 600.0
MAX_REQUESTS = 600  # Maximum number of requests to Graph API per `TIME_AMOUNT` seconds allowed by Facebook.


def load_posts(engine, page_id, access_token, requests_limit, log_config_fname=None):
    global graph
    global logger

    """
    Load data and metadata for all posts on page.
    """

    logger = logging.getLogger('root')

    session = sessionmaker(bind=engine)()
    requests_num = 0
    graph = facebook.GraphAPI(access_token)
    ids = post_ids(graph, page_id)
    if not ids:
        logger.info('No posts found.')
    start = time.time()
    for post_id in ids:
        if session.query(Post).filter_by(fbid=unicode(post_id, 'utf8')).first():
            logger.debug(
                    'Post with ID %s already loaded. Skip.' %
                    post_id)
            continue
        # Query and add post to session.
        requests_num += 1
        try:
            data_dict = _call_and_retry(graph.get_object, 3, post_id, metadata=1)
            try:
                _add_post(session, data_dict)
                # Mark the post as complete (i.e. all the associated data was
                # retrived)
                session.query(Post).filter_by(fbid=unicode(post_id, 'utf8')).update({'incomplete': False})
            except Exception as e:
                logger.exception(e)
                logger.warning('Incomplete data for post with id: %s' % (post_id))
        except Exception as e:
            logger.exception(e)
            logger.warning('Skipped post with id: %s' % (post_id))
            session.add(Post(fbid=unicode(post_id, 'utf8'), incomplete=True))
            session.flush()

        session.commit()
        logger.debug(
                '%s posts loaded, %s seconds passed. ' %
                (requests_num, time.time() - start))
    logger.info('Done in %s seconds.' % (time.time() - start))


def convert_date(date):
    """
    Convert date from ISO-8601 to "%Y-%m-%d %X".
    """
    return parse_date(date).strftime("%Y-%m-%d %X")


def post_ids(graph, page_id, limit=500):
    """
    Generator that returns post IDs ordered descending by
    'create_time' (from newest post to oldest).
    """
    bottom_time = int(round(time.time()))
    while True:
        query = '''
            SELECT post_id, created_time
            FROM stream
            WHERE source_id="%s" AND actor_id="%s" AND created_time < %s
            ORDER BY created_time DESC
            LIMIT %s
        ''' % (page_id, page_id, bottom_time, limit)
        #results = graph.fql({'ids': query})[0]['fql_result_set']
        results = _call_and_retry(graph.fql, 3, {'ids': query})[0]['fql_result_set']
        if not results:
            return
        for result in results:
            bottom_time = result['created_time']
            yield result['post_id']


def _add_post(session, data_dict):

    """
    Add post and related objects from data dict to session
    and flush.

    Do nothing if post with that ID from data dict already exists.
    """

    # Add user.
    if 'from' in data_dict:
        user_data = data_dict['from']
        user, _ = _get_or_create(session, User, fbid=user_data['id'], **user_data)
    else:
        user = User()
    # Add application.
    if 'application' in data_dict:
        app_data = data_dict['application']
        app, _ = _get_or_create(session, Application, fbid=app_data['id'], **app_data)
    else:
        app = Application()
    # Add place.
    if 'place' in data_dict:
        place_data = _clean_place_data(data_dict)
        place, _ = _get_or_create(session, Place, **place_data)
    else:
        place = Place()
    session.flush()

    # Create post.
    post_data = _clean_post_data(data_dict)
    post = Post(
        from_id=user.id,
        application_id=app.id,
        place_id=place.id,
        **post_data)
    session.add(post)
    session.flush()

    # Add post properties.
    if 'properties' in data_dict:
        for property_data in data_dict['properties']:
            property_data = subdict(property_data, Property.__table__.columns.keys())
            session.add(Property(post_id=post.id, **property_data))
    # Add post actions.
    if 'actions' in data_dict:
        for action_data in data_dict['actions']:
            action_data = subdict(action_data, Action.__table__.columns.keys())
            session.add(Action(post_id=post.id, **action_data))
    # Add post metadata.
    if 'metadata' in data_dict:
        if 'connections' in data_dict['metadata']:
            for name, link in data_dict['metadata']['connections'].items():
                session.add(Connection(post_id=post.id, name=name, link=link))
    session.flush()


    # Add post comments.
    if 'comments' in data_dict:
        for comment_data in _get_all(data_dict['id'], 'comments', start_with=data_dict['comments']):
            _add_comments(session, post.id, comment_data)

    # Add post likes.
    if 'likes' in data_dict:
        for like_data in _get_all(data_dict['id'], 'likes', start_with=data_dict['likes']):
            _add_likes(session, post.id, like_data)

    session.flush()

# Adds a new comment to the post with db id = post_id
def _add_comments(session, post_id, comment_data):
    # Get or create commenter.
    commenter_data = comment_data['from']
    commenter, created = _get_or_create(
            session, User, fbid=commenter_data['id'])
    if created:
        commenter.name = commenter_data['name']
        session.flush()
    # Initialize comment to save it further.
    comment_fbid = comment_data['id']
    comment_data = subdict(
            comment_data,
            keys=Comment.__table__.columns.keys(),
            exclude=('id',))
    comment_data['created_time'] = convert_date(comment_data['created_time'])
    session.add(Comment(from_id=commenter.id, fbid=comment_fbid, post_id=post_id, **comment_data))

# Adds a new like to the post with db id = post_id
def _add_likes(session, post_id, like_data):
    # Get or create liker.
    liker, created = _get_or_create(
            session, User, fbid=like_data['id'])
    if created:
        liker.name = like_data['name']
        session.flush()
    session.add(Like(from_id=liker.id, post_id=post_id))

# Recursively gets all the elements of the requested type
# from post with id fb_post_id. the results are returned using yield
def _get_all(fb_post_id, objects_type, after=None, start_with=None):
    global graph
    if start_with is not None:
        for item in start_with['data']:
            yield item
        if 'next' in start_with['paging']:
            for item in _get_all(fb_post_id, objects_type, after=start_with['paging']['cursors']['after']):
                yield item
        return
    if after is not None:
        #additional = graph.request(fb_post_id + '/' + objects_type, {'after':after})
        additional = _call_and_retry(graph.request, 3, fb_post_id + '/' + objects_type, {'after':after})
    else:
        #additional = graph.request(fb_post_id + '/' + objects_type)
        additional = _call_and_retry(graph.request, 3, fb_post_id + '/' + objects_type)

    for item in additional['data']:
        yield item

    if 'next' in additional['paging']:
        for item in _get_all(fb_post_id, objects_type, additional['paging']['cursors']['after']):
            yield item

def _get_or_create(session, model, fbid,  **kwargs):
    instance = session.query(model).filter_by(fbid=fbid).first()
    created = False
    if not instance:
        created = True
        data = subdict(kwargs, keys=model.__table__.columns.keys(), exclude=('id',))
        instance = model(fbid=fbid, **data)
        session.add(instance)
    return instance, created


def _clean_post_data(data_dict):
    """
    Extract post data from data dict.
    """
    data = subdict(data_dict, keys=Post.__table__.columns.keys())
    data['fbid'] = data['id']
    del data['id']
    if 'shares' in data:
        data['shares'] = data['shares']['count']
    data['created_time'] = convert_date(data['created_time'])
    data['updated_time'] = convert_date(data['updated_time'])
    if 'privacy' in data_dict:
        privacy_data = data_dict['privacy']
        if 'value' in privacy_data:
            data['privacy_value'] = privacy_data['value']
        if 'allow' in privacy_data:
            data['allow'] = privacy_data['allow']
        if 'deny' in privacy_data:
            data['deny'] =  privacy_data['deny']
    return data


def _clean_place_data(data_dict):
    """
    Extract place data from data dict.
    """
    place_data = {
        'fbid': data_dict['place']['id'],
        'name': data_dict['place']['name'],
    }
    if 'location' in data_dict['place']:
        place_data.update(data_dict['place']['location'])
    return place_data
