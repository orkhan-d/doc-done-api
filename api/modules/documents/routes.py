import json
import os
from uuid import uuid4
from fastapi import APIRouter, Depends, File, Request, Response, UploadFile, status

from api.dependencies import get_token_header
from api.modules.documents.schemas import AddQueueRow
from api.modules.documents.crud import add_queue_row, get_user_documents

FILES_DIR = os.path.join(os.getcwd(), 'files')
if not os.path.exists(FILES_DIR):
    os.makedirs(FILES_DIR)

router = APIRouter(
    prefix='/queue', tags=['queue'],
    dependencies=[Depends(get_token_header)]
)

@router.post('/add')
async def add_to_queue(
    request: Request,
    data: AddQueueRow = Depends(),
    file: UploadFile = File(...),
    ):
    file_extension = file.filename.split('.')[-1]
    file_name = f'{uuid4()}.{file_extension}'
    with open(os.path.join(FILES_DIR, file_name), 'wb') as f:
        f.write(file.file.read())
    
    add_queue_row(
        json.loads(request.user_data)['id'],
        file_name,
        data.doc_type_id,
        data.fix
    )
    return Response(status_code=status.HTTP_201_CREATED)

@router.get('/')
async def get_queue_files(request: Request,):
    rows = get_user_documents(json.loads(request.user_data)['id'])
    
    return Response([
        {
            'id': r.id,
            'filename': r.doc_name,
            'file_type_id': r.doc_type_id,
            'fix': r.fix,
        } for r in rows
    ],
        status_code=status.HTTP_200_OK
    )