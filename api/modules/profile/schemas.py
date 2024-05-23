from pydantic import BaseModel

class UpdateProfileSchema(BaseModel):
    name: str
    username: str | None
    email: str
    password: str

class SetPremiumSchema(BaseModel):
    days: int