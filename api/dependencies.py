from fastapi import Header
from typing import Annotated

from api.modules.auth.crud import get_user_by_token

async def get_token_header(token: Annotated[str | None, Header()]):
    return get_user_by_token(token)