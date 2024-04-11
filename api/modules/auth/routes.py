from typing import Annotated
from fastapi import APIRouter, Depends

from api.dependencies import get_token_header
from api.modules.auth.crud import add_user, get_user_by_credentials, get_user_token, remove_user_token, set_user_token
from api.modules.auth.models import User
from api.modules.auth.schemas import LoginSchema, SuccessAuthResponse, RegisterSchema, UserInfoSchema

router = APIRouter(prefix='/auth', tags=['auth'])

@router.post('/register', response_model=SuccessAuthResponse)
async def register(data: RegisterSchema):
    user = add_user(**data.model_dump())
    token = set_user_token(user.id)

    return SuccessAuthResponse(
        user=UserInfoSchema(
            id=user.id,
            name=user.name,
            email=user.email,
            token=get_user_token(user.id)
        ),
    )

@router.post('/login', response_model=SuccessAuthResponse)
async def login(data: LoginSchema):
    user = get_user_by_credentials(data.email, data.password)
    token = set_user_token(user.id)

    return SuccessAuthResponse(
        user=UserInfoSchema(
            id=user.id,
            name=user.name,
            email=user.email,
            token=get_user_token(user.id)
        ),
    )

@router.get('/logout')
async def logout(user: Annotated[User, Depends(get_token_header)]):
    remove_user_token(user.id)
    return {"message": "success"}
