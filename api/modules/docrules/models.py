from typing import Any

from sqlalchemy import ForeignKey
from api.db import Base, intpk, Mapped, mapped_column, relationship

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

class Rule(Base):
    __tablename__ = 'rules'

    id: Mapped[intpk]
    name: Mapped[str] = mapped_column(unique=True)
    type: Mapped[str] = mapped_column()
    definition: Mapped[str | None] = mapped_column()
    
    values: Mapped[list["Value"]] = relationship("Value", backref='rule', lazy=True)

    def __init__(self,
                 name: str,
                 type: str
                ):
        self.name = name
        self.type = type

class Value(Base):
    __tablename__ = 'values'

    id: Mapped[intpk]
    value: Mapped[str] = mapped_column(unique=True)
    rule_id: Mapped[int] = mapped_column(ForeignKey('rules.id'))

    def __init__(self,
                 value: str,
                 rule_id: int
                ):
        self.value = value
        self.rule_id = rule_id