#        ~~~      import    ~~~         #
import os
from models import *
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from auth import requires_auth


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    CORS(app)
    setup_db(app)

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type,Authorization')
        response.headers.add('Access-Control-Allow-Method',
                             'GET,DELETE,POST,PATCH')
        return response

#                          ~~~          Actors Endpoints:       ~~~                       #

    @app.route('/')
    def index():
        return 'Hi'

    @app.route('/actors', methods=['GET'])
    @requires_auth('get:retrive_actors')
    def retrive_actors(payload):
        actors = Actors.query.all()
        return jsonify({
            'success': True,
            'Actors': [actor.format() for actor in actors]
        })

    @app.route('/actors/<int:actor_id>', methods=['DELETE'])
    @requires_auth('delete:delete_actor')
    def delete_actor(payload, actor_id):
        try:
            actor = Actors.query.get(actor_id)

            if actor is None:
                abort(404)

            actor.delete()
            actors = Actors.query.all()
            return jsonify({
                'success': True,
                'Actors': [actor.format() for actor in actors]
            })
        except Exception:
            abort(400)

    @app.route('/actors', methods=['POST'])
    @requires_auth('post:add_actor')
    def add_actor(payload):
        try:
            data = request.get_json()
            print(data)
            name = data.get('name', None)
            gender = data.get('gender', None)
            age = data.get('age', None)
            movie_id = data.get('movie_id', None)
            if name is None or age is None or gender is None:
                abort(400)
            actor = Actors(name=name, age=age,
                           gender=gender, movie_id=movie_id)
            actor.insert()
            actors = Actors.query.all()
            return jsonify({
                'success': True,
                'Actors': [actor.format() for actor in actors]
            })
        except Exception:
            abort(400)

    @app.route('/actors/<int:actor_id>', methods=['PATCH'])
    @requires_auth('patch:update_actor')
    def update_actor(payload, actor_id):
        actor = Actors.query.get(actor_id)
        if actor is None:
            abort(404)
        try:
            data = request.get_json()
            new_name = data.get('name')
            new_age = data.get('age')
            new_gender = data.get('gender')
            if new_age is not None:
                actor.age = new_age
            if new_name is not None:
                actor.name = new_name
            if new_gender is not None:
                actor.gender = new_gender
            actor.update()
            actors = Actors.query.all()
            return jsonify({
                'success': True,
                'Actors': [actor.format() for actor in actors]
            })
        except Exception:
            abort(422)

    #                                      ~~~         Movies Endpoints:        ~~~                                  #

    @app.route('/movies', methods=['GET'])
    @requires_auth('get:retrive_movies')
    def retrive_movies(payload):
        movies = Movies.query.all()
        return jsonify({
            'success': True,
            'Movies': [movie.format() for movie in movies]
        })

    @app.route('/movies/<int:movie_id>', methods=['DELETE'])
    @requires_auth('delete:delete_movies')
    def delete_movies(payload, movie_id):
        movie = Movies.query.get(movie_id)
        if movie is None:
            abort(404)
        try:
            movie.delete()
            movies = Movies.query.all()
            return jsonify({
                'success': True,
                'Movies': [movie.format() for movie in movies]
            })
        except Exception:
            abort(422)

    @app.route('/movies', methods=['POST'])
    @requires_auth('post:add_movie')
    def add_movie(payload):
        try:
            data = request.get_json()
            print(data)
            new_title = data.get('title', None)
            new_release_date = data.get('release_date', None)
            if new_title is None or new_release_date is None:
                abort(404)
            movie = Movies(title=new_title, release_date=new_release_date)
            movie.insert()
            movies = Movies.query.all()
            return jsonify({
                'success': True,
                'Movies': [movie.format() for movie in movies]
            })
        except Exception:
            abort(400)

    @app.route('/movies/<int:movie_id>', methods=['PATCH'])
    @requires_auth('patch:update_movie')
    def update_movie(payload, movie_id):
        movie = Movies.query.get(movie_id)
        if movie is None:
            abort(404)
        data = request.get_json()
        new_title = data.get('title', None)
        new_release_date = data.get('release_date', None)
        if new_title is not None:
            movie.title = new_title
        if new_release_date is not None:
            movie.release_date = new_release_date
        try:
            movie.update()
            movies = Movies.query.all()
            return jsonify({
                'success': True,
                'Movies': [movie.format() for movie in movies]
            })
        except Exception:
            abort(422)

    #                                         ~~~       Error Handlers:       ~~~                                   #

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "resource not found"
        }), 404

    @app.errorhandler(500)
    def internal_server_error(error):
        return jsonify({
            "success": False,
            "error": 500,
            "message": "Internal Server Error"
        }), 500

    @app.errorhandler(400)
    def bad_reqeust(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "Bad Reqeust"
        }), 400

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422

    @app.errorhandler(401)
    def Unauthorized(error):
        return jsonify({
            "success": False,
            "error": 401,
            "message": "Unauthorized"
        }), 401

    return app


app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
