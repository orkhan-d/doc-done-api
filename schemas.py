from pydantic import BaseModel

class NotFound(BaseModel):
    code: int = 404
    message: str

    @classmethod
    def what(cls, object: str) -> "NotFound":
        message = f"Such {object} not found!"
        return cls(message=message)