import os
from sqlalchemy import and_
from sqlalchemy.exc import IntegrityError
from api.db import session

from api.modules.documents.models import Queue, dt, UTC
from api.modules.docrules.crud import get_available_docrules
from api.modules.documents.exceptions import WrongFileFormat, DocTypeNotAvailable

FILES_DIR = os.path.join(os.getcwd(), 'files')

def add_queue_row(user_id: int,
                  doc_name: str,
                  doc_type_id: int,
                  fix: bool):
    if doc_name.split('.')[-1]!='docx':
        raise WrongFileFormat()
    if doc_type_id not in [dr.id for dr in get_available_docrules(user_id)]:
        raise DocTypeNotAvailable()
    row = Queue(doc_name,
                user_id,
                doc_type_id,
                fix)
    session.add(row)
    session.commit()
    return row

def remove_old_files(user_id: int):
    rows = session.query(Queue).filter(and_(
        Queue.user_id==user_id,
        Queue.created_at+3*24*60*60<dt.now(UTC).timestamp()
    )).all()
    [session.delete(r) for r in rows]
    session.commit()

def get_user_documents(user_id: int):
    remove_old_files(user_id)
    rows = session.query(Queue).filter(Queue.user_id==user_id).all()
    return rows

def get_file_by_queue_id(q_id: int):
    row = session.query(Queue).filter(Queue.id==q_id).one()
    return row