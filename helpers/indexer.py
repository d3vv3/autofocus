import os
import logging
from helpers.filters import get_type
from helpers.metadata import build_image_item, build_video_item
from database.common import index_item
from datetime import datetime


def index_library(client, library_path: str):
    logging.info('Iterating through library at %s' % library_path)
    dt_1 = datetime.now()
    for subdir, dirs, files in os.walk(library_path):
        for file_name in files:
            file_type = get_type(file_name)
            if file_type != 'other':
                file_path = subdir + os.sep + file_name
                logging.info('Found %s' % file_path)
                item = build_image_item(file_path, file_name) if file_type == 'image' else build_video_item(file_path, file_name)
                index_item(client, 'timeline', item)
    dt_2 = datetime.now()
    time_taken = (dt_2 - dt_1).seconds
    logging.info('Library scanning took %s seconds' % time_taken)


