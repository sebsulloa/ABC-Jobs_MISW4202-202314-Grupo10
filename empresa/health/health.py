from celery import Celery

celery_app = Celery('health', broker='redis://localhost:6379/0')


@celery_app(name='check')
def chequeo_salud():
    