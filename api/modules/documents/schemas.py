from pydantic import BaseModel, Field

class AddQueueRow(BaseModel):
    doc_type_id: int = Field(...)
    fix: bool = Field(...)

class UserQueueRow(BaseModel):
    id: int
    filename: str
    file_type_id: int
    fix: bool
    done: bool

class UserQueueRows(BaseModel):
    files: list[UserQueueRow]