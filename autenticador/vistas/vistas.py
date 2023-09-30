from flask import jsonify
from flask_restful import Resource
from flask_jwt_extended import create_access_token
from celery import Celery

celery_app = Celery(__name__, broker='redis://127.0.0.1:6379/0')

class AuthResource(Resource):
    def get(self):
        access_token = create_access_token(identity="test")
        return jsonify(access_token=access_token)
