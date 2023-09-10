from sqlalchemy import Column, Integer, String
from .declarative_base import Base

class ServiceRegistration(Base):
    __tablename__ = 'service_registration'

    id = Column(Integer, primary_key = True)
    requestId = Column(Integer)
    timestamp = Column(String(200))
    serviceName = Column(String(200))