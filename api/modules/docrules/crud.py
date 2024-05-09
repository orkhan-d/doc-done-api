import os
from sqlalchemy import or_
from sqlalchemy.exc import IntegrityError
from api.db import session
from api.modules.docrules.exceptions import DocRulesExists
from api.modules.docrules.models import DocRule, Rule
from api.exceptions import NotFound

RULES_FILES_DIR = os.path.join(os.getcwd(), 'rule_files')

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

    os.remove(os.path.join(RULES_FILES_DIR, docrules.rules_file))

    session.delete(docrules)
    session.commit()

def get_available_docrules(user_id: int):
    docrules = session.query(DocRule).filter(or_(
        DocRule.user_id==user_id,
        DocRule.user_id.is_(None),
    )).all()
    
    return docrules

def get_rules_db():
    return session.query(Rule).all()

def get_users_custom_docrules(user_id: int):
    return session.query(DocRule).filter(DocRule.user_id==user_id).all()