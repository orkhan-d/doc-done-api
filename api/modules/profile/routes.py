from typing import Annotated
from fastapi import APIRouter, Depends

from api.dependencies import get_token_header
from api.modules.profile.crud import get_user_premium_status, update_user, set_premium
from api.modules.profile.models import User
from api.modules.profile.schemas import UpdateProfileSchema, SetPremiumSchema

router = APIRouter(prefix='/profile', tags=['profile'])

@router.patch('/')
async def update_profile(data: UpdateProfileSchema, user: Annotated[User, Depends(get_token_header)]):
    return update_user(user.id, **data.model_dump())

@router.get('/')
async def get_profile(user: Annotated[User, Depends(get_token_header)]):
    return user

@router.post('/premium')
async def give_premium(data: SetPremiumSchema, user: Annotated[User, Depends(get_token_header)]):
    user = set_premium(user.id, data.days)
    return user

@router.get('/premium')
async def check_premium(user: Annotated[User, Depends(get_token_header)]):
    status, due = get_user_premium_status(user.id)
    return {
        "status": status,
        "due": due
    }