import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import *

Casting_Assistant = os.environ['Casting_Assistant']
Casting_Director = os.environ['Casting_Director']
Executive_Producer = os.environ['Executive_Producer']


class Casting_Agency_TestCase(unittest.TestCase):
    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "casting_agency"
        self.database_path = "postgres://postgres:123456789@{}/{}".format(
            'localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after each test"""
        pass

#     ~~~    retrive actors test case      ~~~     #

    def test_retrive_actors_successTest(self):
        response = self.client().get(
            '/actors', headers={'Authorization': 'bearer ' + Executive_Producer})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['Actors'])


#     ~~~    delete actor test case      ~~~     #


    def test_delete_actor_successTest(self):
        response = self.client().delete(
            '/actors/21', headers={'Authorization': 'bearer ' + Executive_Producer})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['Actors'])

    def Test_delete_actor_errorTest(self):
        response = self.client().delete(
            '/actors/55', headers={'Authorization': 'bearer ' + Casting_Assistant})
        self.assertEqual(response.status_code, 401)

#     ~~~    add actor test case      ~~~     #

    def test_add_actor_successTest(self):
        data = {
            'name': 'bassam',
            'age': 18,
            'gender': 'Male'
        }
        response = self.client().post(
            '/actors', headers={'Authorization': 'bearer ' + Executive_Producer}, json=data)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['Actors'])

    def test_add_actor_errorTest(self):
        data = {
            'name': None,
            'age': 18,
            'gender': 'Male'
        }
        response = self.client().post(
            '/actors', headers={'Authorization': 'bearer ' + Executive_Producer}, json=data)
        self.assertEqual(response.status_code, 400)

#     ~~~    update actor test case      ~~~     #

    def test_update_actor_successTest(self):
        data = {
            'age': 20,
        }
        response = self.client().patch(
            '/actors/5', headers={'Authorization': 'bearer ' + Executive_Producer}, json=data)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['Actors'])

    def test_update_actor_errorTest(self):
        data = {
            'age': 20,
        }
        response = self.client().patch(
            '/actors/5555555', headers={'Authorization': 'bearer ' + Executive_Producer}, json=data)
        self.assertEqual(response.status_code, 404)

#     ~~~    retrive movies test case      ~~~     #

    def test_retrive_movies_successTest(self):
        response = self.client().get(
            '/movies', headers={'Authorization': 'bearer ' + Executive_Producer})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['Movies'])

#     ~~~    delete movies test case      ~~~     #

    def test_delete_movies_successTest(self):
        response = self.client().delete(
            '/movies/7', headers={'Authorization': 'bearer ' + Executive_Producer})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['Movies'])

    def test_delete_movies_errorTest(self):
        response = self.client().delete(
            '/movies/55', headers={'Authorization': 'bearer ' + Executive_Producer})
        self.assertEqual(response.status_code, 404)

#     ~~~    add movies test case      ~~~     #

    def test_add_movie_successTest(self):
        data = {
            'title': 'Spider-Man: Homecoming',
            'release_date': 'July 7, 2017',
        }
        response = self.client().post(
            '/movies', headers={'Authorization': 'bearer ' + Executive_Producer}, json=data)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['Movies'])

    def test_add_movie_errorTest(self):
        data = {
            'title': None,
            'release_date': 18,
        }
        response = self.client().post(
            '/movies', headers={'Authorization': 'bearer ' + Executive_Producer}, json=data)
        self.assertEqual(response.status_code, 400)

#     ~~~    add movies test case      ~~~     #

    def test_update_movie_successTest(self):
        data = {
            'age': 20
        }
        response = self.client().patch(
            '/movies/9', headers={'Authorization': 'bearer ' + Executive_Producer}, json=data)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['Movies'])

    def test_update_movie_errorTest(self):
        data = {
            'age': 20
        }
        response = self.client().patch(
            '/movies/579', headers={'Authorization': 'bearer ' + Executive_Producer}, json=data)
        self.assertEqual(response.status_code, 404)

#     ~~~    Casting Assistant Role test case      ~~~     #
    def test_update_movie_for_Casting_Assistant(self):
        data = {'age': 20}
        response = self.client().patch(
            '/movies/5', headers={'Authorization': 'bearer ' + Casting_Assistant}, json=data)
        self.assertEqual(response.status_code, 401)

    def test_add_movie_for_Casting_Assistant(self):
        data = {
            'title': "ali",
            'release_date': 18
        }
        response = self.client().post(
            '/movies',  headers={'Authorization': 'bearer ' + Casting_Assistant}, json=data)
        self.assertEqual(response.status_code, 401)


#     ~~~    Casting Director Role test case      ~~~     #


    def test_delete_movies_for_Casting_Director(self):
        response = self.client().delete(
            '/movies/6', headers={'Authorization': 'bearer ' + Casting_Director})
        self.assertEqual(response.status_code, 401)

    def test_add_movie_for_Casting_Director(self):
        data = {
            'title': "ali",
            'release_date': 18
        }
        response = self.client().post(
            '/movies',  headers={'Authorization': 'bearer ' + Casting_Director}, json=data)
        self.assertEqual(response.status_code, 401)


#     ~~~    Executive Producer Role test case      ~~~     #


    def test_add_actor_for_Executive_Producer(self):
        data = {
            'name': 'bassam',
            'age': 18,
            'gender': 'Male'
        }
        response = self.client().post(
            '/actors', headers={'Authorization': 'bearer ' + Executive_Producer}, json=data)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['Actors'])

    def test_add_movie_for_Executive_Producer(self):
        data = {
            'title': "ali",
            'release_date': 18,
        }
        response = self.client().post(
            '/movies',  headers={'Authorization': 'bearer ' + Executive_Producer}, json=data)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['Movies'])


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
