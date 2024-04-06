import os
from typing import Annotated
from uuid import uuid4
from sqlalchemy import create_engine
from sqlalchemy.orm import (sessionmaker, scoped_session, DeclarativeBase, 
                            Mapped, mapped_column)

engine = create_engine(os.environ['DB_URL'])
Session = sessionmaker(bind=engine)
session = scoped_session(Session)

class Base(DeclarativeBase): ...

# custom column types
intpk = Annotated[int, mapped_column(primary_key=True)]
uuidpk = Annotated[str, mapped_column(primary_key=True, default=uuid4())]