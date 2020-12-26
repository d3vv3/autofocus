import os
import logging
from helpers import filters


def iterate_library(library_path: str):
    logging.info('Iterating through library at %s' % library_path)
    for subdir, dirs, files in os.walk(library_path):
        for filename in files:
            if filters.get_type(filename) != 'others':
                filepath = subdir + os.sep + filename
                logging.debug('Found %s' % filepath)
