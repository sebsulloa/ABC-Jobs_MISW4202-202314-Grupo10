import datetime
import time
from celery import Celery

celery_app = Celery('health', broker='redis://localhost:6379/0')

def monitor_task(microservice, message):
    # Envía el mensaje a la cola específica del microservicio
    celery_app.send_task('tasks.health_check', args=[message], queue=microservice)

def run_monitor():
    microservices = ['company', 'projects', 'team']

    for i in range(1000):
        for microservice in microservices:
            print(f'{datetime.datetime.now()} {microservice} {i}')
            monitor_task(microservice, i)
        


if __name__ == '__main__':    
    run_monitor()