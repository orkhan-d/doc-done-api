from typing import Any, Dict
from fastapi.exceptions import HTTPException

class DocRulesExists(HTTPException):
    def __init__(self, headers: Dict[str, str] | None = None) -> None:
        super().__init__(422, {
            "name": "Docrules with such name already exists"
        }, headers)