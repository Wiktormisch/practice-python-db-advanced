from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Measurment(Base):
    __tablename__ = "measurments"
    id = Column(Integer, primary_key=True)
    device_name = Column(String, nullable=False)
    value = Column(Float, nullable=False)
    timestamp = Column(DateTime, nullable=False)