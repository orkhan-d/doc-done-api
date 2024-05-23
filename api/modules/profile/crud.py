from api.db import session
from api.modules.profile.exceptions import AuthError
from api.modules.profile.models import User

from datetime import timedelta as td, datetime as dt

def update_user(
        user_id: int, *,
        name: str,
        username: str,
        email: str,
        password: str) -> User:
    user = session.query(User).filter(User.id == user_id).first()
    if not user:
        raise AuthError()
    user.name = name
    user.username = username
    user.email = email
    user.password = password
    
    session.commit()
    return session.query(User).filter(User.id == user_id).one()

def set_premium(user_id: int, days: int) -> User:
    user = session.query(User).filter(User.id == user_id).first()
    if not user:
        raise AuthError()
    
    user.is_premium = True
    user.is_premium_due = dt.now() + td(days=days)
    
    session.commit()
    return session.query(User).filter(User.id == user_id).one()

def get_user_premium_status(user_id: int) -> tuple[bool | None, dt | None]:
    user = session.query(User).filter(User.id == user_id).first()
    if not user:
        raise AuthError()
    
    return user.is_premium, user.is_premium_due