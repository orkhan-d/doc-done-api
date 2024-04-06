from typing import Any
from api.db import Base, intpk, Mapped, mapped_column

class DocRule(Base):
    __tablename__ = 'docrules'

    id: Mapped[intpk]
    name: Mapped[str] = mapped_column(unique=True)
    user_id: Mapped[int | None] = mapped_column()
    rules_file: Mapped[str] = mapped_column()

    def __init__(self,
                 name: str,
                 user_id: int | None,
                 rules_file: str):
        self.name = name
        self.user_id = user_id
        self.rules_file = rules_file