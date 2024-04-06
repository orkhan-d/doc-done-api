from typing import Dict
from fastapi.exceptions import HTTPException

class WrongFileFormat(HTTPException):
    def __init__(self, headers: Dict[str, str] | None = None) -> None:
        super().__init__(422, {
            "file": "File has wrong format! Provide .docx file"
        }, headers)

class DocTypeNotAvailable(HTTPException):
    def __init__(self, headers: Dict[str, str] | None = None) -> None:
        super().__init__(422, {
            "file": "Such document type is not available for you!"
        }, headers)