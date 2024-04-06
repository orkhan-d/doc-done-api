from typing import Any, Dict
from typing_extensions import Annotated
from fastapi.exceptions import HTTPException

class NotFound(HTTPException):
    def __init__(self, what: str, headers: Dict[str, str] | None = None) -> None:
        super().__init__(404, {
            "message": f"Such {what} not found!"
        }, headers)