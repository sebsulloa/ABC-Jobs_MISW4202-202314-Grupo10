import datetime
from celery import Celery
import random

celery_app = Celery('health', broker='redis://localhost:6379/0')

celery_app.conf.task_queues = {
    'company': {
        'exchange': 'company',
        'exchange_type': 'direct',
        'routing_key': 'company',
    }
}

@celery_app.task(name='tasks.health_check', queue='company')
def check(message):
    
    random_number = random.random()

    if random_number <= 0.9:
        celery_app.send_task('tasks.health_response', args=['company', message], queue='monitor')
        