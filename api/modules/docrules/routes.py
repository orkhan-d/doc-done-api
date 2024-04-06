import json
import os
from uuid import uuid4
from fastapi import APIRouter, Depends, Request

from api.dependencies import get_token_header
from api.modules.docrules.crud import add_docrules, remove_docrules
from api.modules.docrules.schemas import AddDocRuleSchema

RULES_FILES_DIR = os.path.join(os.getcwd(), 'rule_files')
if not os.path.exists(RULES_FILES_DIR):
    os.makedirs(RULES_FILES_DIR)

router = APIRouter(
    prefix='/docrules', tags=['docrules'],
    dependencies=[Depends(get_token_header)]
)

@router.post('/add')
async def register(data: AddDocRuleSchema, request: Request):
    dict_data = data.model_dump()
    rules = dict_data['data']
    absolute_file_name = f'{uuid4()}.json'

    json.dump(
        rules,
        open(os.path.join(RULES_FILES_DIR, absolute_file_name), 'w')
    )

    add_docrules(data.name, json.loads(request.user_data)['id'], absolute_file_name)

@router.post('/{docrule_id}/remove')
async def login(docrule_id: int):
    remove_docrules(docrule_id)