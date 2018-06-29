import datetime
import os
from sqlalchemy import create_engine, Column, Integer, Boolean, Unicode, Sequence, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine(os.environ.get("POSTGRES_URL"), echo=True)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Ilumination(Base):
    
    __tablename__ = 'ilumination'

    id = Column(Integer,
            Sequence('ilumination_id_seq'), primary_key=True)
    value = Column(Boolean)
    created_date = Column(DateTime, default=datetime.datetime.utcnow)

Base.metadata.create_all(engine)