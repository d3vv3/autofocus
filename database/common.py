import pymongo
import logging


def create_database(client, database_name: str):
    try:
        client[database_name]
        logging.debug('Database %s created in MongoDB' % database_name)
        return database_name
    except:
        logging.error('Could not create database in MongoDB')
        return False

def create_collection(client, database_name: str, collection_name: str):
    try:
        client[database_name][collection_name]
        logging.debug('Collection %s was created in %s' % (collection_name,
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
