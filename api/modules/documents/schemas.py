from typing import Any
from pydantic import BaseModel, Field

class AddQueueRow(BaseModel):
    doc_type_id: int = Field(...)
    fix: bool = Field(...)