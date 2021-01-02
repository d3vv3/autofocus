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


def paginated_column(client, db_name: str, collection_name: str, column_name: str,
            page_size: int, page_num: int):
    '''
    returns a set of documents belonging to page number `page_num`
    where size of each page is `page_size`.
    '''
    # Calculate number of documents to skip
    skips = page_size * (page_num - 1)

    # Skip and limit
    cursor = client[db_name][collection_name].find(
            {},
            {column_name: 1}).skip(skips).limit(page_size)
    data = [x for x in cursor]
    last_id = skips + len(data)
    max_id = cursor.count()
    if not data:
        return None
    # Return documents
    return data, last_id, max_id