from uuid import uuid4
from sqlalchemy.exc import IntegrityError
from sqlalchemy import and_
from api.db import session
from api.modules.auth.exceptions import AuthError, EmailExists
from api.modules.auth.models import User

def add_user(name: str, email: str, password: str):
    try:
        user = User(name, email, password)
        session.add(user)
        session.commit()
        return user
    except IntegrityError as e:
        session.rollback()
        raise EmailExists()

def get_user_by_credentials(email: str, password: str):
    user = session.query(User).filter(and_(
        User.email==email,
        User.password==password,
    )).first()
    if not user:
        raise AuthError()
    return user

def get_user_by_token(token: str | None):
    if token is None:
        raise AuthError()
    user = session.query(User).filter(User.token==token).first()
    if not user:
        raise AuthError()
    return user

def set_user_token(uid: int) -> str:
    user = session.query(User).filter(User.id==uid).first()
    if not user:
        raise AuthError()

    token = str(uuid4())
    user.token = token
    print(token)
    session.commit()
    return token

def get_user_token(uid: int) -> str | None:
    user = session.query(User).filter(User.id==uid).first()
    if not user:
        raise AuthError()

    return user.token

def remove_user_token(uid: int):
    user = session.query(User).filter(User.id==uid).first()
    if not user:
        raise AuthError()

    user.token = None
    session.commit()
