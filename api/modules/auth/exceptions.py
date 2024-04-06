from typing import Any, Dict
from typing_extensions import Annotated, Doc
from fastapi.exceptions import HTTPException

class AuthError(HTTPException):
    def __init__(self, headers: Dict[str, str] | None = None) -> None:
        super().__init__(401, {
            "message": "Autharization error!",
        }, headers)

class EmailExists(HTTPException):
    def __init__(self, headers: Dict[str, str] | None = None) -> None:
        super().__init__(422, {
            "email": "Such email already exists"
        }, headers)