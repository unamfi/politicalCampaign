import logging
from sqlalchemy.orm import sessionmaker
import facebook

from models import User
from common import _call_and_retry

graph = None


def update_user_data(user, new_data):
    '''Updates the user object with interesting data from new_data'''
    logger = logging.getLogger('root')
    if 'relationship_status' in new_data:
        logger.info('relationship_status available for user {0} : {1}'.format(user.fbid, new_data['relationship_status']))
    if 'age_range' in new_data:
        logger.info('Age_range available for user {0} : {1}'.format(user.fbid, new_data['age_range']))
    for f in ['first_name', 'last_name', 'gender', 'relationship_status']:
        if f in new_data:
            setattr(user, f, new_data[f])

def get_user_data(user_fbid):
    '''Retrieves the interesting fields from the user's public profile.

    The request is retried for 3 times before failing.

    Returnes a dict containing user information or None if it wan't retrieved.'''
    global graph
    logger = logging.getLogger('root')
    try:
        return _call_and_retry(graph.get_object, 3, user_fbid, fields='id,first_name,last_name,relationship_status,gender,age_range')
    except Exception as e:
        logger.exception(e)
        logger.warning('Unable to retrieve profile for user with fbid={0}'.format(user_fbid))
        return None


def retrieve_users(engine, access_token):
    '''Retrieve additional data about the users and update the rows.

    This function selects all the User objects which miss all the additional data.
    Queries are sent to facebook for each such user and the responses are recorded in the DB.'''
    global graph
    graph = facebook.GraphAPI(access_token)
    session = sessionmaker(bind=engine)()
    all_users = session.query(User).filter((User.first_name == None) &
                                           (User.last_name == None) &
                                           (User.gender == None) &
                                           (User.relationship_status == None)
                                           ).all()
    for user in all_users:
        user_data = get_user_data(user.fbid)
        if user_data:
            update_user_data(user, user_data)
            session.commit()
