from sqlalchemy import ForeignKey
from api.db import Base, intpk, Mapped, mapped_column

from datetime import datetime as dt, UTC

class Queue(Base):
    __tablename__ = 'queue'

    id: Mapped[intpk]
    doc_name: Mapped[str] = mapped_column(unique=True)
    user_id: Mapped[int] = mapped_column()
    doc_type_id: Mapped[int] = mapped_column(ForeignKey('docrules.id'))
    fix: Mapped[bool] = mapped_column()

    created_at: Mapped[int] = mapped_column(default=int(dt.now(UTC).timestamp()))

    def __init__(self,
                 doc_name: str,
                 user_id: int,
                 doc_type_id: int,
                 fix: bool):
        self.doc_name = doc_name
        self.user_id = user_id
        self.doc_type_id = doc_type_id
        self.fix = fix