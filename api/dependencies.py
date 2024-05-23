import json
from fastapi import Header, Request
from typing import Annotated

from api.modules.auth.crud import get_user_by_token

async def get_token_header(token: Annotated[str | None, Header()], request: Request):
    user = get_user_by_token(token)
    try:
        request.user_data = json.dumps({ # type: ignore
            'id': user.id,
            'name': user.name,
            'email': user.email,
        })
    except Exception as e:
        print(e)
    
    return user