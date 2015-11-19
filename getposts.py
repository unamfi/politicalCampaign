#!/usr/bin/env python

import ConfigParser
import logging.config
import sqlalchemy
import sys

import encodings
encodings._aliases["utf8mb4"] = "utf_8"

reload(sys)
sys.setdefaultencoding("utf-8")

from sqlalchemy import create_engine

from fbtools import MAX_REQUESTS
from fbtools import load_posts

import common

import fb_user
from models import create_tables


if __name__ == '__main__':
    # Read configuration file.
    if len(sys.argv) != 2 and len(sys.argv) != 3:
        print('Usage: ./getposts.py config_file [--users]')
        exit()
    config = ConfigParser.RawConfigParser()
    config_filename = sys.argv[1]
    config.read(config_filename)

    # Load logging settings.
    logging.config.fileConfig(config_filename)
    logger = logging.getLogger('root')

    # Validate data in config.
    access_token = config.get('facebook', 'access_token')
    if not access_token:
        logger.error('You must specify access token in config.')
        exit()
    page_id = config.get('facebook', 'page_id')
    if not page_id.isdigit():
        logger.error('Page ID must be numeric.')
        exit()
    requests_limit = config.getint('script', 'requests_limit')
    if requests_limit > MAX_REQUESTS or requests_limit <= 0:
        logger.error('Number of requests must be in range [0..%s], got: %s.' %
                     (MAX_REQUESTS, requests_limit))
        exit()

    # Get DB data and create tables that don't exist.
    dbuser = config.get('mysql', 'user')
    dbpass = config.get('mysql', 'password')
    dbname = config.get('mysql', 'dbname')
    dbhost = config.get('mysql', 'host')
    connect_string = 'mysql://{user}:{password}@{host}/{dbname}?charset=utf8mb4'.format(
        user=dbuser, password=dbpass, host=dbhost, dbname=dbname)
    engine = create_engine(connect_string)
    try:
        create_tables(dbuser, dbpass, dbname, engine, dbhost)
    except sqlalchemy.exc.OperationalError, e:
        logger.error('Failed to connect to DB: %s.' % e.args)
        exit()

    common.delays_gen = common.delays(requests_limit, 600.0)

    if len(sys.argv) == 2:
        load_posts(engine, page_id, access_token,
                   requests_limit, config_filename)
    elif sys.argv[2] == '--users':
        logger.debug('get user infos')
        fb_user.retrieve_users(engine, access_token)
    else:
        logger.error('Unknown option {}'.format(sys.argv[2]))
