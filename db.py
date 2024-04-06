import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, DeclarativeBase

engine = create_engine(os.environ['DB_URL'])
Session = sessionmaker(bind=engine)
session = scoped_session(Session)

class Base(DeclarativeBase): ...