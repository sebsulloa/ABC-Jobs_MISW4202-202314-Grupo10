import datetime
import time
from models.declarative_base import Base, engine, session
from models.models import *
from celery import Celery

celery_app = Celery('health', broker='redis://localhost:6379/0')

def monitor_task(microservice, message):
    # Envía el mensaje a la cola específica del microservicio
    celery_app.send_task('tasks.health_check', args=[message], queue=microservice)

def run_monitor(session):
    microservices = ['company', 'projects', 'team']

    for i in range(1000):
        for microservice in microservices:
            print(f'{datetime.datetime.now()} {microservice} {i}')
            monitor_task(microservice, i)
        time.sleep(0.25)

        for microservice in microservices:
            microserviceData = session.query(MonitorRegistration).filter(MonitorRegistration.serviceName == microservice).first()

            if(microserviceData.lastReceived != i):
                failure = FailureRegistration(requestId = i, timestamp=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), serviceName=microservice)
                session.add(failure)
                session.commit()
                session.close()

            microserviceData.lastSent = i + 1
            session.commit()
            session.close()


if __name__ == '__main__':
    Base.metadata.create_all(engine)

    session.query(MonitorRegistration).delete()
    session.query(ServiceRegistration).delete()
    session.query(FailureRegistration).delete()

    company = MonitorRegistration(lastSent='0', lastReceived='-1', serviceName='company')
    projects = MonitorRegistration(lastSent='0', lastReceived='-1', serviceName='projects')
    team = MonitorRegistration(lastSent='0', lastReceived='-1', serviceName='team')

    session.add(company)
    session.add(projects)
    session.add(team)
    session.commit()
    session.close()
    
    run_monitor(session)