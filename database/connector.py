import logging
import sys
from pymongo import MongoClient


def connect_mongo(db_url: str):
    logging.info('Connecting to MongoDB')
    try:
        client = MongoClient(db_url, connect=False)
    except:
        logging.error('Could not connect to MongoDB')
        sys.exit()
    return client


def create_mongo_url(ip: str,
                        port: str,
                        user: str,
                        password: str):
    url = 'mongodb://%s:%s@%s:%s/' % (user, password, ip, port)
    logging.debug('MongoDB url is %s' % url)
    return url