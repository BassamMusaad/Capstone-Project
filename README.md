# Full Stack Capstone Project (Casting Agency)

## Introduction

Casting-Agency is the final project in Udacity Nanodgree. The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies.

The main motivation behind this project is to use all the knowledge that was learned from Udacity's FSND Course


## Getting Started 

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## Running the server

first ensure you are working using your created virtual environment.

To run the server, execute:

On Windows :
``` 
-set FLASK_APP=app
-flask run app --host=127.0.0.1 --port=8080 --reload
```
On Linux/MAC :
``` 
-export FLASK_APP=app
-flask run app --host=127.0.0.1 --port=8080 --reload
```

### This Appliaction Works On Heroku Cloud:
- URL: https://capstone-bassam.herokuapp.com/

# API Reference:

## Getting Started:

- Base URL: This application hosted at 

- Authentication: This application require authentication .

## Authentication

Based on the specific role you would like to test for, each of the roles has a jwt token that is available in the setup.sh file in the parent directory of this repository.

This app has 3 Roles. Each has his own token which are provided in setup.sh file.

### Roles

**Casting Assistant :**
- view:actors
- view:movies

**Casting Director :** 
- All permissions a Casting Assistant has
- create:actor
- delete:actor
- update:actor
- update:movie

**Executive Producer :**
- All permissions a Casting Director has
- add:movie
- delete:movie



## Error Handling:

Errors are returned as JSON in the following format.

```
{
    "success": False,
    "error": 404,
    "message": "resource not found"
}
```
#### The API will return three types of errors:

- 400 – bad request
- 401 - Unauthorized
- 404 – resource not found
- 422 – unprocessable
- 500 - Internal Server Error

## Endpoints:

#### GET '/actors'
- Fetch all Actors information
- Returns: JSON response containing all actors information, request status 
- Request Arguments: None
- Example response: 
```
{
    'success' : True,
    'Actors' : [
        {
            'name' : 'bassam',
            'age' : 22,
            'gender' : 'Male'
        },
        ...
    ]
}
```

#### DELETE '/actors/actor_id'
- Delete an existing actor from the database
- Request Arguments:<int:actor_id>
- Example response:
```
{
    'success' : True,
    'Actors' : [
        {
            'name' : 'bassam',
            'age' : 22,
            'gender' : 'Male'
        },
        ...
    ]
}
```

#### POST '/actors'
-  Add a new actor to the database
-  Request body: <string:name, int:age, string:gender>
-  Example response:
```
{
  'success': True,
  'Actors' : [
        {
            'name' : 'bassam',
            'age' : 22,
            'gender' : 'Male'
        },
        ...
    ]  
}
```

#### UPDATE '/actors/actor_id'
- Update the actor on the database
- Request body: <int:actor_id>
- Example response:
```
{
   'success': True,
   'Actors' : [
        {
            'name' : 'bassam',
            'age' : 22,
            'gender' : 'Male'
        },
        ...
    ] 
}
```




#### GET '/movies'
- Fetch all movies information 
- Request Arguments:None
- Example response:
```
{
    'success' : True,
    'Movies' : [
        {
            'title' : 'Spider-Man: Homecoming',
            'release_date' : 'July 7, 2017'
        },
        ...
    ]
}
```


#### DELETE '/movies/movie_id'
- Delete an existing movie from the database
- Request body: <int:movie_id>
- Example response:
```
{
    'success' : True,
    'Movies' : [
        {
            'title' : 'Spider-Man: Homecoming',
            'release_date' : 'July 7, 2017'
        },
        ...
    ]
}
```

#### POST '/movies'
- add new movie to database
- Request body: <String:title,String:release_date>
- Example response:
```
{
    'success' : True,
    'Movies' : [
        {
            'title' : 'Spider-Man: Homecoming',
            'release_date' : 'July 7, 2017'
        },
        ...
    ]
}
```



#### UPDATE '/movies/movie_id'
- update an existing movie on database
- Request body: <String:title,String:release_date>
- Example response:
```
{
    'success' : True,
    'Movies' : [
        {
            'title' : 'Spider-Man: Homecoming',
            'release_date' : 'July 7, 2017'
        },
        ...
    ]
}
```


## Testing

To run the tests, run

```
- python test_app.py
```
