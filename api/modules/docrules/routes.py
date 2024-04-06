import json
import os
from uuid import uuid4
from fastapi import APIRouter, Depends, Request
from fastapi.responses import JSONResponse

from api.dependencies import get_token_header
from api.modules.docrules.crud import add_docrules, get_users_custom_docrules, remove_docrules
from api.modules.docrules.schemas import AddDocRuleSchema, DocRulesInfo, DocRuleInfo

RULES_FILES_DIR = os.path.join(os.getcwd(), 'rule_files')
if not os.path.exists(RULES_FILES_DIR):
    os.makedirs(RULES_FILES_DIR)

router = APIRouter(
    prefix='/docrules', tags=['docrules'],
    dependencies=[Depends(get_token_header)]
)

@router.post('/add')
async def add_docrule(data: AddDocRuleSchema, request: Request):
    dict_data = data.model_dump()
    rules = dict_data['data']
    absolute_file_name = f'{uuid4()}.json'

    json.dump(
        rules,
        open(os.path.join(RULES_FILES_DIR, absolute_file_name), 'w')
    )

    add_docrules(data.name, json.loads(request.user_data)['id'], absolute_file_name)

@router.get('/{docrule_id}/remove')
async def remove_docrule(docrule_id: int):
    remove_docrules(docrule_id)

@router.get('/', response_model=DocRulesInfo)
async def get_users_docrules(request: Request):
    return JSONResponse(
        DocRulesInfo(docrules=[
            DocRuleInfo(name=dr.name)
            for dr in get_users_custom_docrules(json.loads(request.user_data)['id'])
        ]).model_dump()
    )