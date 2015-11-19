# vim: set fileencoding=utf-8 fileformat=unix :

from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import Unicode
from sqlalchemy import UnicodeText
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Post(Base):

    __tablename__ = 'post'

    id = Column(Integer, primary_key=True)

    application_id = Column(Integer, ForeignKey('application.id'))
    caption = Column(UnicodeText)
    created_time = Column(DateTime)
    updated_time = Column(DateTime)
    description = Column(UnicodeText)
    from_id = Column(Integer, ForeignKey('user.id'))
    icon = Column(UnicodeText)
    fbid = Column(Unicode(41), unique=True)    # 'id' field in JSON.
    is_hidden = Column(Boolean)
    link = Column(UnicodeText)
    name = Column(UnicodeText)   # Name of the link.
    message = Column(UnicodeText)
    object_id = Column(Unicode(20))  # ID of photo or video in post.
    picture = Column(UnicodeText)
    place_id = Column(Integer, ForeignKey('place.id'))

    # Privacy fields.
    privacy_value = Column(Unicode(18))
    allow = Column(UnicodeText)    # Comma-separated list of friends.
    deny = Column(UnicodeText)

    shares = Column(Integer)
    source = Column(UnicodeText)
    status_type = Column(Unicode(25))
    type = Column(Unicode(20))    # 'type' field in JSON.
    story = Column(UnicodeText)
    # TODO: Add following fields: to, message_tags, story_tags, with_tags.

    incomplete = Column(Boolean, default=True)


class Action(Base):

    __tablename__ = 'action'

    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('post.id'))
    name = Column(UnicodeText)
    link = Column(UnicodeText)


class Application(Base):

    __tablename__ = 'application'

    id = Column(Integer, primary_key=True)
    fbid = Column(Unicode(20), unique=True)    # 'id' field in JSON.
    name = Column(UnicodeText)


class Comment(Base):

    __tablename__ = 'comment'

    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('post.id'))
    # 'id' field in JSON. Not unique. Facebook can return the same comment for
    # different posts.
    fbid = Column(Unicode(41))
    from_id = Column(Integer, ForeignKey('user.id'))
    message = Column(UnicodeText)
    can_remove = Column(Boolean)
    created_time = Column(DateTime)
    like_count = Column(Integer)
    user_likes = Column(Boolean)


class Like(Base):

    __tablename__ = 'fb_likes'

    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('post.id'))
    from_id = Column(Integer, ForeignKey('user.id'))


class Property(Base):

    __tablename__ = 'property'

    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('post.id'))
    name = Column(Unicode(40))
    text = Column(UnicodeText)


class Place(Base):

    __tablename__ = 'place'

    id = Column(Integer, primary_key=True)
    fbid = Column(Unicode(20), unique=True)
    name = Column(UnicodeText)
    street = Column(UnicodeText)
    zip = Column(UnicodeText)
    latitude = Column(Float)
    longitude = Column(Float)


class User(Base):

    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    fbid = Column(Unicode(20), unique=True)
    name = Column(UnicodeText)
    first_name = Column(UnicodeText)
    last_name = Column(UnicodeText)
    gender = Column(Unicode(50))
    relationship_status = Column(Unicode(100))


class Connection(Base):

    __tablename__ = 'connection'

    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('post.id'))
    name = Column(Unicode(50))    # ['comments', 'insights', 'likes']
    link = Column(UnicodeText)


def create_tables(user, password, dbname,
                  engine, host='localhost', dialect='mysql'):
    """
    Create tables which don't exist.
    """
    Base.metadata.create_all(engine)
