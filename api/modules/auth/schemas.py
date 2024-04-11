from pydantic import BaseModel

class LoginSchema(BaseModel):
    email: str
    password: str

class RegisterSchema(BaseModel):
    name: str
    email: str
    password: str

class UserInfoSchema(BaseModel):
    id: int
    name: str
    email: str
    token: str | None

class SuccessAuthResponse(BaseModel):
    user: UserInfoSchema