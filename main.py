import os
import logging
import multiprocessing as mp

from api.server import start_api_server


if __name__ == '__main__':

    # Start the server API
    p = mp.Process(target=start_api_server)
    p.start()
