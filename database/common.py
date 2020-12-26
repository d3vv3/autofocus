import pymongo
import logging


def create_database(client, database_name: str):
    try:
        client[database_name]
        logging.info('Database %s created in MongoDB' % database_name)
        return database_name
    except:
        logging.error('Could not create database in MongoDB')
        return False

def create_collection(client, database_name: str, collection_name: str):
    try:
        client[database_name][collection_name]
        logging.info('Collection %s was created in %s' % (collection_name,
                                                           database_name))
        return collection_name
    except:
        logging.error('Database %s is not in MongoDB' % database_name)
        return False

def create_structure(client):
    database_name = create_database(client, 'autofocus')
    collections = ['timeline', 'people', 'albums']
    for collection in collections:
        create_collection(client, database_name, collection)
    return True


def index_item(client, collection_name: str, item: dict):
    try:
        collection = client['autofocus'][collection_name]
        collection.insert_one(item)
        logging.info('Item %s was inserted into %s' % (item, collection_name))
        return True
    except:
        logging.warning('Item %s could not be inserted into %s' % (item,
                                                                   collection_name))
        return False