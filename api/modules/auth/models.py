from typing import Any
from api.db import Base, intpk, Mapped, mapped_column

from datetime import datetime as dt

class User(Base):
    __tablename__ = 'users'

    id: Mapped[intpk]
    name: Mapped[str] = mapped_column()
    username: Mapped[str | None] = mapped_column()
    is_premium: Mapped[bool | None] = mapped_column(default=False)
    is_premium_due: Mapped[dt | None] = mapped_column()
    email: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str] = mapped_column()
    token: Mapped[str | None] = mapped_column()

    def __init__(self,
                 name: str,
                 username: str,
                 email: str,
                 password: str):
        self.name = name
        self.username = username
        self.email = email
        self.password = password