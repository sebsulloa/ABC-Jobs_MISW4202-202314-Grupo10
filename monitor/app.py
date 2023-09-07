from monitor import create_app
from flask_restful import Resource, Api
from flask import Flask, request
from celery import Celery

celery_app = Celery('health', broker='redis://localhost:6379/0')

app = create_app('default')
app_context = app.app_context()
app_context.push()

@celery_app(name='check')
def chequeo_salud():
    pass

class VistaMonitor(Resource):
    def get(self):
        microservices = ['service_empresa', 'service_proyectp', 'service_equipo']
        chequeo_salud.delay()
        return {'message': 'Chequeo iniciado'}, 200

api = Api(app)
api.add_resource(VistaMonitor, '/monitor')
