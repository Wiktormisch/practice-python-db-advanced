from db import Session, engine
from models import Base, Note
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

Base.metadata.create_all(engine) 
