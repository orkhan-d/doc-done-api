from typing import Any
from api.db import Base, intpk, Mapped, mapped_column

class User(Base):
    __tablename__ = 'users'

    id: Mapped[intpk]
    name: Mapped[str] = mapped_column()
    email: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str] = mapped_column()
    token: Mapped[str | None] = mapped_column()

    def __init__(self,
                 name: str,
                 email: str,
                 password: str):
        self.name = name
        self.email = email
        self.password = password