from sqlalchemy import or_
from sqlalchemy.exc import IntegrityError
from api.db import session
from api.modules.docrules.exceptions import DocRulesExists
from api.modules.docrules.models import DocRule
from api.exceptions import NotFound

def add_docrules(name: str, user_id: int | None, rules_file: str):
    try:
        docrules = DocRule(name, user_id, rules_file)
        session.add(docrules)
        session.commit()
        return docrules
    except IntegrityError as e:
        session.rollback()
        raise DocRulesExists()

def remove_docrules(id_: int):
    docrules = session.query(DocRule).filter(DocRule.id==id_).first()
    if not docrules:
        raise NotFound('docrule')

    session.delete(docrules)

def get_available_docrules(user_id: int):
    docrules = session.query(DocRule).filter(or_(
        DocRule.user_id==user_id,
        DocRule.user_id.is_(None),
    )).all()
    
    return docrules