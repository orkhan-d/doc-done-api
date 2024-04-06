from typing import Any
from pydantic import BaseModel

class Rule(BaseModel):
    name: str
    value: list[Any] | str | int

class TextFormatRules(BaseModel):
    text_format: str
    rules: list[Rule]

class AddDocRuleSchema(BaseModel):
    name: str
    data: list[TextFormatRules]