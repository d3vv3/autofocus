from fastapi import FastAPI, Response
import uvicorn
from multiprocessing import Process
import logging

from helpers.indexer import index_library
from helpers.thumbnails import thumbnail_generator
from setup import mongo_client, library, api_port, log_level, cores, thumbnails, batch_number

app = FastAPI()


def start_api_server():
    ''' Start the server api, meant to run on a separate process '''
    uvicorn.run(app, port=api_port, log_level=log_level.lower())


@app.get("/")
async def read_root():
    return {'Hello': 'World'}

@app.get('/index/{method}', status_code=200)
async def index(method: str, response: Response):
    '''
    Spawn the indexer in another thread so the api is not slowed down
    '''
    try:
        if method == "quick":
            p = Process(target=index_library, args=(mongo_client, library,))
            p.start()
            return {'message': 'Indexing has started'}
        if method == "full":
            # TODO: Index and scan for faces and objects
            response.status_code = 501
            return {'message': 'Not implemented yet'}
        else:
            response.status_code = 405
    except:
        response.status_code = 500
        return {'message': 'There was an error on starting indexer'}
    
@app.get('/create_thumbnails', status_code=200)
async def create_thumbnails(response: Response):
    '''
    Spawn the thumbnail generator in another thread so the api is not slowed down
    '''
    try:
        p = Process(target=thumbnail_generator, args=(mongo_client, cores, thumbnails, batch_number))
        p.start()
        return {'message': 'Thumbnails creation has started'}
    except Exception as e:
        response.status_code = 500
        logging.error("There was an error on starting the generation of thumbnails")
        logging.error(e)
        return {'message': 'There was an error on starting the generation of thumbnails'}


