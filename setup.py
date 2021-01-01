import os
import logging
from dotenv import load_dotenv
from database.connector import connect_mongo, create_mongo_url
from database.common import create_structure


def setup_mongodb():

    # Get database config
    db_ip = os.environ.get('MONGODB_IP', None)
    assert db_ip is not None
    db_port = os.environ.get('MONGODB_PORT', None)
    assert db_port is not None
    db_user = os.environ.get('MONGODB_USER', None)
    assert db_user is not None
    db_password = os.environ.get('MONGODB_PASSWORD', None)
    assert db_password is not None

    # Connect to mongodb
    url = create_mongo_url(db_ip, db_port, db_user, db_password)
    client = connect_mongo(url)
    create_structure(client)

    return client


def setup_library():

    # Get images library
    library = os.environ.get('IMAGES_LIBRARY', None)
    assert library is not None

    return library

def setup_api():

    api_port = int(os.environ.get('API_PORT', 9000))

    return api_port


def setup_logging():

    # Get logging config
    log_file = os.environ.get('LOG_FILE', 'autofocus.log')
    assert log_file is not None
    log_level = os.environ.get('LOG_LEVEL', 'INFO')
    assert log_level is not None

    # Configure logging
    logging.basicConfig(filename=log_file,
                        format='%(asctime)s %(levelname)s %(message)s',
                        datefmt='%d/%m/%Y %I:%M:%S',
                        level=log_level)
    return log_level


def setup():

    # Get .env file
    load_dotenv()

    log_level = setup_logging()
    mongo_client = setup_mongodb()
    library = setup_library()
    api_port = setup_api()

    return mongo_client, library, api_port, log_level


mongo_client, library, api_port, log_level = setup()