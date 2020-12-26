# deIndex server

Server for deIndex.


### What is deIndex?

deIndex server is a fast, light, scalable, photo indexer.


### How are we indexing?

We are indexing images by:

* Faces: using some fast 'face_recognition' library.
* Places: on a map and quering for names of location coordinates.
* Object recognition: using some YOLO v3 model or others.
* Others: tags will be added automatically or by hand (optional).

This implies if you search for `red car` you will get the results from the most  
matches to the least (till no matches).


### Performance

We are building a blazing fast and light server, in order to be able to run it  
on as many computers as possible. Even if they are old.


### Tools

We have chosen to build deIndex using:

* Python: the language I mostly speak.
* ReactJS: so our web is responsive, functional and scalable.
* Flutter: so our app feels native everywhere.

Obviously the tools are not everything. Code must be built efficiently.

### Install (development)
1. Install `face_recognition` from [here](https://github.com/ageitgey/face_recognition#installation) (dlib included).
2. Install requirements by `pip install -r requirements.txt`.
3. Deploy mongodb with `docker run -d --name mongo -p 27017:27017 -e MONGO_INITDB_ROOT_USERNAME=autofocus -e MONGO_INITDB_ROOT_PASSWORD=apassword mongo`
4. Edit the `.env` file for your setup.
5. Start developing!