import os
from PIL import Image
from itertools import product
import logging
from datetime import datetime
from multiprocessing import Pool

from database.common import paginated_column
from helpers.filters import get_type

def generate_thumbnail(image_details):
    size, file_path, thumbnails = image_details
    filename = os.path.basename(file_path)
    if get_type(filename) is not 'image':
        return
    thumbnail_filename = "%s_%s" % (size[1], filename)
    try:
        im = Image.open(file_path)
        im.thumbnail(size)
        im.save(os.path.join(thumbnails, thumbnail_filename))
        return
    except Exception as e:
        logging.warning('Could not generate thumbnail with res %s for %s' % (size, filename))
        logging.warning(e)
        return


def thumbnail_generator(client, cores, thumbnails, batch_number):
    logging.info('Generating thumbnails for the library')
    dt_1 = datetime.now()
    sizes = [(120,120), (300,300), (500,500)]
    page, last_id, max_id = 1, 0, 1
    while last_id < max_id:
        files, last_id, max_id = paginated_column(client, 'autofocus', 'timeline', 'path',
                                                  batch_number, page)
        print("PAGE:", page, "LAST_ID:", last_id, "MAX_ID:", max_id)
        if files is None:
            return
        page = page + 1
        files = [doc['path'] for doc in files]
        pool = Pool(cores)
        results = pool.map(generate_thumbnail, list(product(sizes, files, [thumbnails])))
    dt_2 = datetime.now()
    time_taken = (dt_2 - dt_1).seconds
    logging.info('Thumbnail generator took %s seconds' % time_taken)