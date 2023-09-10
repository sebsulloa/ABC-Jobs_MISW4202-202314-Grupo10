from sqlalchemy import Column, Integer, String
from .declarative_base import Base

class MonitorRegistration(Base):
    __tablename__ = 'monitor_registration'
    
    id = Column(Integer, primary_key = True)
    lastSent = Column(Integer)
    lastReceived = Column(Integer)
    serviceName = Column(String(200))

class ServiceRegistration(Base):
    __tablename__ = 'service_registration'

    id = Column(Integer, primary_key = True)
    requestId = Column(Integer)
    timestamp = Column(String(200))
    serviceName = Column(String(200))

class FailureRegistration(Base):
    __tablename__ = 'failure_registration'

    id = Column(Integer, primary_key = True)
    requestId = Column(Integer)
    timestamp = Column(String(200))
    serviceName = Column(String(200))