from celery import Celery
from ..models.declarative_base import Base, engine, session
from ..models.models import *

celery_app = Celery('health', broker='redis://localhost:6379/0')

celery_app.conf.task_queues = {
    'monitor': {
        'exchange': 'monitor',
        'exchange_type': 'direct',
        'routing_key': 'monitor',
    }
}

Base.metadata.create_all(engine)

@celery_app.task(name='tasks.health_response', queue='monitor')
def check(microservice, message): 
    microserviceData = session.query(MonitorRegistration).filter(MonitorRegistration.serviceName == microservice).first()
    microserviceData.lastReceived = message
    print(f'recibido DB {microserviceData.serviceName} {message}')
    session.commit()
    session.close()