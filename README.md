# AirBnB Clone - The Console
The console is the first segment of the AirBnB project at Holberton School that will collectively cover fundamental concepts of higher level programming. The goal of AirBnB project is to eventually deploy our server a simple copy of the AirBnB Website(HBnB). A command interpreter is created in this segment to manage objects for the AirBnB(HBnB) website.

#### Functionalities of this command interpreter:
* Create a new object (ex: a new User or a new Place)
* Retrieve an object from a file, a database etc...
* Do operations on objects (count, compute stats, etc...)
* Update attributes of an object
* Destroy an object

## Table of Content
* [Environment](#environment)
* [Installation](#installation)
* [File Descriptions](#file-descriptions)
* [Usage](#usage)
* [Examples of use](#examples-of-use)
* [Bugs](#bugs)
* [Authors](#authors)
* [License](#license)

## Environment
This project is interpreted/tested on Ubuntu 14.04 LTS using python3 (version 3.4.3)

## Installation
* Clone this repository: `git clone "https://github.com/alexaorrico/AirBnB_clone.git"`
* Access AirBnb directory: `cd AirBnB_clone`
* Run hbnb(interactively): `./console` and enter command
* Run hbnb(non-interactively): `echo "<command>" | ./console.py`

## File Descriptions
[console.py](console.py) - the console contains the entry point of the command interpreter. 
List of commands this console current supports:
* `EOF` - exits console 
* `quit` - exits console
* `<emptyline>` - overwrites default emptyline method and does nothing
* `create` - Creates a new instance of`BaseModel`, saves it (to the JSON file) and prints the id
* `destroy` - Deletes an instance based on the class name and id (save the change into the JSON file). 
* `show` - Prints the string representation of an instance based on the class name and id.
* `all` - Prints all string representation of all instances based or not on the class name. 
* `update` - Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file). 

#### `models/` directory contains classes used for this project:
[base_model.py](/models/base_model.py) - The BaseModel class from which future classes will be derived
* `def __init__(self, *args, **kwargs)` - Initialization of the base model
* `def __str__(self)` - String representation of the BaseModel class
* `def save(self)` - Updates the attribute `updated_at` with the current datetime
* `def to_dict(self)` - returns a dictionary containing all keys/values of the instance

Classes inherited from Base Model:
* [amenity.py](/models/amenity.py)
* [city.py](/models/city.py)
* [place.py](/models/place.py)
* [review.py](/models/review.py)
* [state.py](/models/state.py)
* [user.py](/models/user.py)

#### `/models/engine` directory contains File Storage class that handles JASON serialization and deserialization :
[file_storage.py](/models/engine/file_storage.py) - serializes instances to a JSON file & deserializes back to instances
* `def all(self)` - returns the dictionary __objects
* `def new(self, obj)` - sets in __objects the obj with key <obj class name>.id
* `def save(self)` - serializes __objects to the JSON file (path: __file_path)
* ` def reload(self)` -  deserializes the JSON file to __objects

#### `/tests` directory contains all unit test cases for this project:
[/test_models/test_base_model.py](/tests/test_models/test_base_model.py) - Contains the TestBaseModel and TestBaseModelDocs classes
TestBaseModelDocs class:
* `def setUpClass(cls)`- Set up for the doc tests
* `def test_pep8_conformance_base_model(self)` - Test that models/base_model.py conforms to PEP8
* `def test_pep8_conformance_test_base_model(self)` - Test that tests/test_models/test_base_model.py conforms to PEP8
* `def test_bm_module_docstring(self)` - Test for the base_model.py module docstring
* `def test_bm_class_docstring(self)` - Test for the BaseModel class docstring
* `def test_bm_func_docstrings(self)` - Test for the presence of docstrings in BaseModel methods

TestBaseModel class:
* `def test_is_base_model(self)` - Test that the instatiation of a BaseModel works
* `def test_created_at_instantiation(self)` - Test created_at is a pub. instance attribute of type datetime
* `def test_updated_at_instantiation(self)` - Test updated_at is a pub. instance attribute of type datetime
* `def test_diff_datetime_objs(self)` - Test that two BaseModel instances have different datetime objects

[/test_models/test_amenity.py](/tests/test_models/test_amenity.py) - Contains the TestAmenityDocs class:
* `def setUpClass(cls)` - Set up for the doc tests
* `def test_pep8_conformance_amenity(self)` - Test that models/amenity.py conforms to PEP8
* `def test_pep8_conformance_test_amenity(self)` - Test that tests/test_models/test_amenity.py conforms to PEP8
* `def test_amenity_module_docstring(self)` - Test for the amenity.py module docstring
* `def test_amenity_class_docstring(self)` - Test for the Amenity class docstring

[/test_models/test_city.py](/tests/test_models/test_city.py) - Contains the TestCityDocs class:
* `def setUpClass(cls)` - Set up for the doc tests
* `def test_pep8_conformance_city(self)` - Test that models/city.py conforms to PEP8
* `def test_pep8_conformance_test_city(self)` - Test that tests/test_models/test_city.py conforms to PEP8
* `def test_city_module_docstring(self)` - Test for the city.py module docstring
* `def test_city_class_docstring(self)` - Test for the City class docstring

[/test_models/test_file_storage.py](/tests/test_models/test_file_storage.py) - Contains the TestFileStorageDocs class:
* `def setUpClass(cls)` - Set up for the doc tests
* `def test_pep8_conformance_file_storage(self)` - Test that models/file_storage.py conforms to PEP8
* `def test_pep8_conformance_test_file_storage(self)` - Test that tests/test_models/test_file_storage.py conforms to PEP8
* `def test_file_storage_module_docstring(self)` - Test for the file_storage.py module docstring
* `def test_file_storage_class_docstring(self)` - Test for the FileStorage class docstring

[/test_models/test_place.py](/tests/test_models/test_place.py) - Contains the TestPlaceDoc class:
* `def setUpClass(cls)` - Set up for the doc tests
* `def test_pep8_conformance_place(self)` - Test that models/place.py conforms to PEP8.
* `def test_pep8_conformance_test_place(self)` - Test that tests/test_models/test_place.py conforms to PEP8.
* `def test_place_module_docstring(self)` - Test for the place.py module docstring
* `def test_place_class_docstring(self)` - Test for the Place class docstring

[/test_models/test_review.py](/tests/test_models/test_review.py) - Contains the TestReviewDocs class:
* `def setUpClass(cls)` - Set up for the doc tests
* `def test_pep8_conformance_review(self)` - Test that models/review.py conforms to PEP8
* `def test_pep8_conformance_test_review(self)` - Test that tests/test_models/test_review.py conforms to PEP8
* `def test_review_module_docstring(self)` - Test for the review.py module docstring
* `def test_review_class_docstring(self)` - Test for the Review class docstring

[/test_models/state.py](/tests/test_models/test_state.py) - Contains the TestStateDocs class:
* `def setUpClass(cls)` - Set up for the doc tests
* `def test_pep8_conformance_state(self)` - Test that models/state.py conforms to PEP8
* `def test_pep8_conformance_test_state(self)` - Test that tests/test_models/test_state.py conforms to PEP8
* `def test_state_module_docstring(self)` - Test for the state.py module docstring
* `def test_state_class_docstring(self)` - Test for the State class docstring

[/test_models/user.py](/tests/test_models/test_user.py) - Contains the TestUserDocs class:
* `def setUpClass(cls)` - Set up for the doc tests
* `def test_pep8_conformance_user(self)` - Test that models/user.py conforms to PEP8
* `def test_pep8_conformance_test_user(self)` - Test that tests/test_models/test_user.py conforms to PEP8
* `def test_user_module_docstring(self)` - Test for the user.py module docstring
* `def test_user_class_docstring(self)` - Test for the User class docstring


## Examples of use
```
vagrantAirBnB_clone$./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) all MyModel
** class doesn't exist **
(hbnb) create BaseModel
7da56403-cc45-4f1c-ad32-bfafeb2bb050
(hbnb) all BaseModel
[[BaseModel] (7da56403-cc45-4f1c-ad32-bfafeb2bb050) {'updated_at': datetime.datetime(2017, 9, 28, 9, 50, 46, 772167), 'id': '7da56403-cc45-4f1c-ad32-bfafeb2bb050', 'created_at': datetime.datetime(2017, 9, 28, 9, 50, 46, 772123)}]
(hbnb) show BaseModel 7da56403-cc45-4f1c-ad32-bfafeb2bb050
[BaseModel] (7da56403-cc45-4f1c-ad32-bfafeb2bb050) {'updated_at': datetime.datetime(2017, 9, 28, 9, 50, 46, 772167), 'id': '7da56403-cc45-4f1c-ad32-bfafeb2bb050', 'created_at': datetime.datetime(2017, 9, 28, 9, 50, 46, 772123)}
(hbnb) destroy BaseModel 7da56403-cc45-4f1c-ad32-bfafeb2bb050
(hbnb) show BaseModel 7da56403-cc45-4f1c-ad32-bfafeb2bb050
** no instance found **
(hbnb) quit
```

## Bugs
No known bugs at this time. 

## Authors
Alexa Orrico - [Github](https://github.com/alexaorrico) / [Twitter](https://twitter.com/alexa_orrico)  
Jennifer Huang - [Github](https://github.com/jhuang10123) / [Twitter](https://twitter.com/earthtojhuang)
Michael Murithi - [Github](https://github.com/mikelexx) / [LinkedIn](https://www.linkedin.com/in/murithimichael254/)

Second part of Airbnb: Joann Vuong
## License
Public Domain. No copy write protection. 

Third part of AirBnb: Michael Murithi
Concepts
For this project, we expect you to look at these concepts:

- [REST API](https://intranet.alxswe.com/concepts/45)
- [AirBnB clone](https://intranet.alxswe.com/concepts/74)
**Resources**
Read or watch:

- REST API concept page
- [Learn REST: A RESTful Tutorial](https://intranet.alxswe.com/rltoken/rycjU2GvZAlahHa61WWDBg)
- [Designing a RESTful API with Python and Flask](https://intranet.alxswe.com/rltoken/WfKwKtaROCybta0_E849AQ)
- [HTTP access control (CORS)](https://intranet.alxswe.com/rltoken/D55IFF8lgZDLPyIX6b6C5A)
- [Flask cheatsheet](https://intranet.alxswe.com/rltoken/L01qANfgx0al8_an4mtPuw)
- [What are Flask Blueprints, exactly?](https://intranet.alxswe.com/rltoken/QxbV8TCzNl3oP9br8CV5Lw)
- [Flask](https://intranet.alxswe.com/rltoken/OLWDl7iDVpWKykekaznWpQ)
- [Modular Applications with Blueprints](https://intranet.alxswe.com/rltoken/y3Lhj6w1g59MA_HPtc578w)
- [Flask tests](https://intranet.alxswe.com/rltoken/UGo4ArPFHhx-ow2QtZWILA)
- [Flask-CORS](https://intranet.alxswe.com/rltoken/vq8ER3xb99-N2anC-zke3A)
**Learning Objectives**
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

General
- What REST means
- What API means
- What CORS means
- What is an API
- What is a REST API
- What are other type of APIs
- Which is the HTTP method to retrieve resource(s)
- Which is the HTTP method to create a resource
- Which is the HTTP method to update resource
- Which is the HTTP method to delete resource
- How to request REST API

**More Info**
-[web flow illustration diagram](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/02078cd7f0573885c85a225c7436584a5afea1f9.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240523%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240523T033714Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=9385d195587302d5647b2a5d1e4b4600b785750212cad9fb321dce327999ac08)

**Install Flask**
```
 pip3 install Flask==3
 ```
**Tasks**

0. Restart from scratch!
mandatory
No no no! We are already too far in the project to restart everything.

But once again, let’s work on a new codebase.

For this project you will fork this [codebase](https://github.com/alexaorrico/AirBnB_clone_v2.git):

- Update the repository name to `AirBnB_clone_v3`
- Update the `README.md`:
	- Add yourself as an author of the project
	- Add new information about your new contribution
	- Make it better!
- If you’re the owner of this codebase, create a new repository called `AirBnB_clone_v3` and copy over all files from `AirBnB_clone_v2`

1. Never fail!
mandatory

Since the beginning we’ve been using the `unittest` module, but do you know why unittests are so important? Because when you add a new feature, you refactor a piece of code, etc… you want to be sure you didn’t break anything.

At Holberton, we have a lot of tests, and they all pass! Just for the Intranet itself, there are:

- `5,213` assertions (as of 08/20/2018)
- `13,061` assertions (as of 01/25/2021)
The following requirements must be met for your project:

- all current tests must pass (don’t delete them…)
- add new tests as much as you can (tests are mandatory for some tasks)
```
guillaume@ubuntu:~/AirBnB_v3$ python3 -m unittest discover tests 2>&1 | tail -1
OK
guillaume@ubuntu:~/AirBnB_v3$ HBNB_ENV=test HBNB_MYSQL_USER=hbnb_test HBNB_MYSQL_PWD=hbnb_test_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_test_db HBNB_TYPE_STORAGE=db python3 -m unittest discover tests 2>&1 /dev/null | tail -n 1
OK
guillaume@ubuntu:~/AirBnB_v3$
```

2. Improve storage
mandatory
Update `DBStorage` and `FileStorage`, adding two new methods. All changes should be done in the branch storage_get_count:

A method to retrieve one object:
- 
- Prototype: `def get(self, cls, id):`
	- `cls`: class
	- `id`: string representing the object ID
- Returns the object based on the class and its ID, or `None` if not found
A method to count the number of objects in storage:

- Prototype: `def count(self, cls=None):`
	- `cls`: class (optional)
- Returns the number of objects in storage matching the given class. If no class is passed, returns the count of all objects in storage.
Don’t forget to add new tests for these 2 methods on each storage engine.

```
guillaume@ubuntu:~/AirBnB_v3$ cat test_get_count.py
#!/usr/bin/python3
""" Test .get() and .count() methods
"""
from models import storage
from models.state import State

print("All objects: {}".format(storage.count()))
print("State objects: {}".format(storage.count(State)))

first_state_id = list(storage.all(State).values())[0].id
print("First state: {}".format(storage.get(State, first_state_id)))

guillaume@ubuntu:~/AirBnB_v3$
guillaume@ubuntu:~/AirBnB_v3$ HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./test_get_count.py 
All objects: 1013
State objects: 27
First state: [State] (f8d21261-3e79-4f5c-829a-99d7452cd73c) {'name': 'Colorado', 'updated_at': datetime.datetime(2017, 3, 25, 2, 17, 6), 'created_at': datetime.datetime(2017, 3, 25, 2, 17, 6), '_sa_instance_state': <sqlalchemy.orm.state.InstanceState object at 0x7fc0103a8e80>, 'id': 'f8d21261-3e79-4f5c-829a-99d7452cd73c'}
guillaume@ubuntu:~/AirBnB_v3$
guillaume@ubuntu:~/AirBnB_v3$ ./test_get_count.py 
All objects: 19
State objects: 5
First state: [State] (af14c85b-172f-4474-8a30-d4ec21f9795e) {'updated_at': datetime.datetime(2017, 4, 13, 17, 10, 22, 378824), 'name': 'Arizona', 'id': 'af14c85b-172f-4474-8a30-d4ec21f9795e', 'created_at': datetime.datetime(2017, 4, 13, 17, 10, 22, 378763)}
guillaume@ubuntu:~/AirBnB_v3$ 
```
For this task, you *must* make a pull request on GitHub.com, and ask at least one of your peer to review and merge it.

File: `models/engine/db_storage.py, models/engine/file_storage.py, tests/test_models/test_engine/test_db_storage.py, tests/test_models/test_engine/test_file_storage.py`

3. Status of your API
mandatory
It’s time to start your API!

Your first endpoint (route) will be to return the status of your API:
```
guillaume@ubuntu:~/AirBnB_v3$ HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db HBNB_API_HOST=0.0.0.0 HBNB_API_PORT=5000 python3 -m api.v1.app
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
...
```
In another terminal:
```
guillaume@ubuntu:~/AirBnB_v3$ curl -X GET http://0.0.0.0:5000/api/v1/status
{
  "status": "OK"
}
guillaume@ubuntu:~/AirBnB_v3$
guillaume@ubuntu:~/AirBnB_v3$ curl -X GET -s http://0.0.0.0:5000/api/v1/status -vvv 2>&1 | grep Content-Type
< Content-Type: application/json
guillaume@ubuntu:~/AirBnB_v3$
```
Magic right? (No need to have a pretty rendered output, it’s a JSON, only the structure is important)

Ok, let starts:

- Create a folder `api` at the root of the project with an empty file `__init__.py`
- Create a folder `v1` inside `api`:
- create an empty file ` __init__.py`
- create a file `app.py`:
- create a variable `app`, instance of `Flask`
- import `storage` from `models`
- import `app_views` from `api.v1.views`
- register the blueprint `app_views` to your Flask instance `app`
- declare a method to handle `@app.teardown_appcontext` that calls` storage.close()`
- inside `if __name__ == "__main__":`, run your Flask server (variable `app`) with:
- host = environment variable `HBNB_API_HOST` or `0.0.0.0` if not defined
- port = environment variable `HBNB_API_PORT` or `5000` if not defined
- `threaded=True`
- Create a folder `views` inside `v1`:
- create a file `__init__.py`:
- import `Blueprint` from `flask doc`
- create a variable `app_views` which is an instance of `Blueprint` (url prefix must be `/api/v1`)
- wildcard import of everything in the package `api.v1.views.index` => PEP8 will complain about it, don’t worry, it’s normal and this file (`v1/views/__init__.py`) won’t be check.
- create a file `index.py`
- import `app_views` from `api.v1.views`
- create a route `/status` on the object `app_views` that returns a JSON: `"status": "OK"` (see example)
File: `api/__init__.py, api/v1/__init__.py, api/v1/views/__init__.py, api/v1/views/index.py, api/v1/app.py`

4. Some stats?
mandatory
Create an endpoint that retrieves the number of each objects by type:

- `In api/v1/views/index.py`
- Route: `/api/v1/stats`
- You must use the newly added `count()` method from storage
```
guillaume@ubuntu:~/AirBnB_v3$ curl -X GET http://0.0.0.0:5000/api/v1/stats
{
  "amenities": 47,
  "cities": 36,
  "places": 154,
  "reviews": 718,
  "states": 27,
  "users": 31
}
guillaume@ubuntu:~/AirBnB_v3$
```
FILE: `api/v1/views/index.py`
(No need to have a pretty rendered output, it’s a JSON, only the structure is important)

5. Not found
mandatory
Designers are really creative when they have to design a “404 page”, a “Not found”… [34 brilliantly designed 404 error pages](https://intranet.alxswe.com/rltoken/8NwELW0j77kZ1jTM6hJFhA)

Today it’s different, because you won’t use HTML and CSS, but JSON!

In `api/v1/app.py`, create a handler for `404` errors that returns a JSON-formatted `404` status code response. The content should be: `"error": "Not found"`
```
guillaume@ubuntu:~/AirBnB_v3$ curl -X GET http://0.0.0.0:5000/api/v1/nop
{
  "error": "Not found"
}
guillaume@ubuntu:~/AirBnB_v3$ curl -X GET http://0.0.0.0:5000/api/v1/nop -vvv
*   Trying 0.0.0.0...
* TCP_NODELAY set
* Connected to 0.0.0.0 (127.0.0.1) port 5000 (#0)
> GET /api/v1/nop HTTP/1.1
> Host: 0.0.0.0:5000
> User-Agent: curl/7.51.0
> Accept: */*
> 
* HTTP 1.0, assume close after body
< HTTP/1.0 404 NOT FOUND
< Content-Type: application/json
< Content-Length: 27
< Server: Werkzeug/0.12.1 Python/3.4.3
< Date: Fri, 14 Apr 2017 23:43:24 GMT
< 
{
  "error": "Not found"
}
guillaume@ubuntu:~/AirBnB_v3$ 
```

6. State
mandatory
Create a new view for `State` objects that handles all default RESTFul API actions:

- In the file `api/v1/views/states.py`
- You must use `to_dict()` to retrieve an object into a valid JSON
- Update `api/v1/views/__init__.py` to import this new file
Retrieves the list of all `State` objects: `GET /api/v1/states`

Retrieves a `State` object: `GET /api/v1/states/<state_id>`

- If the `state_id` is not linked to any `State` object, raise a `404` error
Deletes a State object:: `DELETE /api/v1/states/<state_id>`
- If the `state_id` is not linked to any `State` object, raise a `404` error
- Returns an empty dictionary with the status code `200`
Creates a State: `POST /api/v1/states`

- You must use `request.get_json` from Flask to transform the HTTP body request to a dictionary
- If the HTTP body request is not valid JSON, raise a `400` error with the message `Not a JSON`
- If the dictionary doesn’t contain the key name, raise a 400 error with the message `Missing name`
- Returns the new `State` with the status code `201`
Updates a State object:` PUT /api/v1/states/<state_id>`

- If the `state_id` is not linked to any State object, raise a `404` error
- You must use `request.get_json` from Flask to transform the HTTP body request to a dictionary
- If the HTTP body request is not valid JSON, raise a `400` error with the message `Not a JSON`
- Update the `State` object with all key-value pairs of the dictionary.
- Ignore keys:` id, created_at` and `updated_at`
- Returns the `State` object with the status code `200`
```
guillaume@ubuntu:~/AirBnB_v3$ curl -X GET http://0.0.0.0:5000/api/v1/states/
[
  {
    "__class__": "State",
    "created_at": "2017-04-14T00:00:02",
    "id": "8f165686-c98d-46d9-87d9-d6059ade2d99",
    "name": "Louisiana",
    "updated_at": "2017-04-14T00:00:02"
  },
  {
    "__class__": "State",
    "created_at": "2017-04-14T16:21:42",
    "id": "1a9c29c7-e39c-4840-b5f9-74310b34f269",
    "name": "Arizona",
    "updated_at": "2017-04-14T16:21:42"
  },
...
guillaume@ubuntu:~/AirBnB_v3$
guillaume@ubuntu:~/AirBnB_v3$ curl -X GET http://0.0.0.0:5000/api/v1/states/8f165686-c98d-46d9-87d9-d6059ade2d99
 {
  "__class__": "State",
  "created_at": "2017-04-14T00:00:02",
  "id": "8f165686-c98d-46d9-87d9-d6059ade2d99",
  "name": "Louisiana",
  "updated_at": "2017-04-14T00:00:02"
}
guillaume@ubuntu:~/AirBnB_v3$
guillaume@ubuntu:~/AirBnB_v3$ curl -X POST http://0.0.0.0:5000/api/v1/states/ -H "Content-Type: application/json" -d '{"name": "California"}' -vvv
*   Trying 0.0.0.0...
* TCP_NODELAY set
* Connected to 0.0.0.0 (127.0.0.1) port 5000 (#0)
> POST /api/v1/states/ HTTP/1.1
> Host: 0.0.0.0:5000
> User-Agent: curl/7.51.0
> Accept: */*
> Content-Type: application/json
> Content-Length: 22
>
* upload completely sent off: 22 out of 22 bytes
* HTTP 1.0, assume close after body
< HTTP/1.0 201 CREATED
< Content-Type: application/json
< Content-Length: 195
< Server: Werkzeug/0.12.1 Python/3.4.3
< Date: Sat, 15 Apr 2017 01:30:27 GMT
<
{
  "__class__": "State",
  "created_at": "2017-04-15T01:30:27.557877",
  "id": "feadaa73-9e4b-4514-905b-8253f36b46f6",
  "name": "California",
  "updated_at": "2017-04-15T01:30:27.558081"
}
* Curl_http_done: called premature == 0
* Closing connection 0
guillaume@ubuntu:~/AirBnB_v3$
guillaume@ubuntu:~/AirBnB_v3$ curl -X PUT http://0.0.0.0:5000/api/v1/states/feadaa73-9e4b-4514-905b-8253f36b46f6 -H "Content-Type: application/json" -d '{"name": "California is so cool"}'
{
  "__class__": "State",
  "created_at": "2017-04-15T01:30:28",
  "id": "feadaa73-9e4b-4514-905b-8253f36b46f6",
  "name": "California is so cool",
  "updated_at": "2017-04-15T01:51:08.044996"
}
guillaume@ubuntu:~/AirBnB_v3$
guillaume@ubuntu:~/AirBnB_v3$ curl -X GET http://0.0.0.0:5000/api/v1/states/feadaa73-9e4b-4514-905b-8253f36b46f6
{
  "__class__": "State",
  "created_at": "2017-04-15T01:30:28",
  "id": "feadaa73-9e4b-4514-905b-8253f36b46f6",
  "name": "California is so cool",
  "updated_at": "2017-04-15T01:51:08"
}
guillaume@ubuntu:~/AirBnB_v3$
guillaume@ubuntu:~/AirBnB_v3$ curl -X DELETE http://0.0.0.0:5000/api/v1/states/feadaa73-9e4b-4514-905b-8253f36b46f6
{}
guillaume@ubuntu:~/AirBnB_v3$
guillaume@ubuntu:~/AirBnB_v3$ curl -X GET http://0.0.0.0:5000/api/v1/states/feadaa73-9e4b-4514-905b-8253f36b46f6
{
  "error": "Not found"
}
guillaume@ubuntu:~/AirBnB_v3$
```
File: `api/v1/views/states.py, api/v1/views/__init__.py`

7. City
mandatory
Same as `State`, create a new view for `City` objects that handles all default RESTFul API actions:

- In the file `api/v1/views/cities.py`
- You must use `to_dict()` to serialize an object into valid JSON
- Update `api/v1/views/__init__.py` to import this new file
Retrieves the list of all `City` objects of a `State: GET /api/v1/states/<state_id>/cities`

- If the `state_id` is not linked to any State object, raise a `404` error
Retrieves a `City` object. : `GET /api/v1/cities/<city_id>`
- If the `city_id` is not linked to any `City` object, raise a `404` error
Deletes a `City` object: `DELETE /api/v1/cities/<city_id>`	

- If the `city_id` is not linked to any `City` object, raise a `404` error
Returns an empty dictionary with the status code `200`
Creates a `City`: `POST /api/v1/states/<state_id>/cities`
- 
- You must use `request.get_json` from Flask to transform the HTTP body request to a dictionary
- If the `state_id` is not linked to any State object, raise a `404` error
- If the HTTP body request is not a valid JSON, raise a `400` error with the `message Not a JSON`
- If the dictionary doesn’t contain the key `name`, raise a `400` error with the message `Missing name`
- Returns the new `City` with the status code `201`
Updates a `City` object: `PUT /api/v1/cities/<city_id>`

- If the `city_id` is not linked to any City object, raise a `404` error
- You must use `request.get_json` from Flask to transform the HTTP body request to a dictionary
- If the HTTP request body is not valid JSON, raise a `400` error with the message `Not a JSON`
- Update the `City` object with all key-value pairs of the dictionary
- Ignore keys:` id, state_id, created_at` and `updated_at`
- Returns the `City` object with the status code `200`

11. Reviews
mandatory
Create a new view for `Review` object that handles all default RESTFul API actions:

In the file `api/v1/views/places_reviews.py`
You must use `to_dict()` to retrieve an object into valid JSON
Update `api/v1/views/__init__.py` to import this new file
Retrieves the list of all `Review` objects of a `Place`: `GET /api/v1/places/<place_id>/reviews`

If the `place_id` is not linked to any `Place` object, raise a `404` error
Retrieves a `Review` object. : `GET /api/v1/reviews/<review_id>`

If the `review_id` is not linked to any `Review` object, raise a `404` error
Deletes a `Review` object:` DELETE /api/v1/reviews/<review_id>`

If the `review_id` is not linked to any `Review` object, raise a `404` error
Returns an empty dictionary with the status code `200`
Creates a `Review`: `POST /api/v1/places/<place_id>/reviews`

You must use `request.get_json` from Flask to transform the HTTP request to a dictionary
If the `place_id` is not linked to any `Place` object, raise a `404` error
If the HTTP body request is not valid JSON, raise a `400` error with the message `Not a JSON`
If the dictionary doesn’t contain the key `user_id`, raise a `400` error with the message `Missing user_id`
If the `user_id` is not linked to any `User` object, raise a `404` error
If the dictionary doesn’t contain the key `text`, raise a `400` error with the message `Missing text`
Returns the new `Review` with the status code `201`
Updates a `Review` object: `PUT /api/v1/reviews/<review_id>`

If the `review_id` is not linked to any `Review` object, raise a `404` error
You must use `request.get_json` from Flask to transform the HTTP request to a dictionary
If the HTTP request body is not valid JSON, raise a `400` error with the message `Not a JSON`
Update the `Review` object with all key-value pairs of the dictionary
Ignore keys: `id`, `user_id`, `place_id`, `created_at` and `updated_at`
Returns the `Review` object with the status code `200`
```

File: `api/v1/views/places_reviews.py, api/v1/views/__init__.py`

12. HTTP access control (CORS)
mandatory
A resource makes a cross-origin HTTP request when it requests a resource from a different domain, or port, than the one the first resource itself serves.

Read the full definition [here](https://intranet.alxswe.com/rltoken/D55IFF8lgZDLPyIX6b6C5A)

Why do we need this?

Because you will soon start allowing a web client to make requests your API. If your API doesn’t have a correct CORS setup, your web client won’t be able to access your data.

With Flask, it’s really easy, you will use the class `CORS` of the module `flask_cors`.

How to install it: $ `pip3 install flask_cors`

Update api/v1/app.py to create a CORS instance allowing:`/*` for `0.0.0.0`

You will update it later when you will deploy your API to production.

Now you can see this HTTP Response Header:` < Access-Control-Allow-Origin: 0.0.0.0`
```
guillaume@ubuntu:~/AirBnB_v3$ curl -X GET http://0.0.0.0:5000/api/v1/cities/1da255c0-f023-4779-8134-2b1b40f87683 -vvv
*   Trying 0.0.0.0...
* TCP_NODELAY set
* Connected to 0.0.0.0 (127.0.0.1) port 5000 (#0)
> GET /api/v1/states/2b9a4627-8a9e-4f32-a752-9a84fa7f4efd/cities/1da255c0-f023-4779-8134-2b1b40f87683 HTTP/1.1
> Host: 0.0.0.0:5000
> User-Agent: curl/7.51.0
> Accept: */*
>
* HTTP 1.0, assume close after body
< HTTP/1.0 200 OK
< Content-Type: application/json
< Access-Control-Allow-Origin: 0.0.0.0
< Content-Length: 236
< Server: Werkzeug/0.12.1 Python/3.4.3
< Date: Sun, 16 Apr 2017 04:20:13 GMT
<
{
  "__class__": "City",
  "created_at": "2017-03-25T02:17:06",
  "id": "1da255c0-f023-4779-8134-2b1b40f87683",
  "name": "New Orleans",
  "state_id": "2b9a4627-8a9e-4f32-a752-9a84fa7f4efd",
  "updated_at": "2017-03-25T02:17:06"
}
* Curl_http_done: called premature == 0
* Closing connection 0
guillaume@ubuntu:~/AirBnB_v3$
```
File: `api/v1/app.p`
