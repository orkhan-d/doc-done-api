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

class SuccessAuthResponse(BaseModel):
    user: UserInfoSchema
    token: str | None

class AuthErrorResponse(BaseModel):
    code: int = 401
    message: str = "Invalid credentials!"