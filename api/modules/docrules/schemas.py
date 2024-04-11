from typing import Any
from pydantic import BaseModel

class Rule(BaseModel):
    name: str
    value: list[Any] | str | int

class TextFormatRules(BaseModel):
    text_type: str
    name: str
    value: str

class AddDocRuleSchema(BaseModel):
    name: str
    rules: list[TextFormatRules]

class DocRuleInfo(BaseModel):
    id: int
    name: str

class DocRulesInfo(BaseModel):
    docrules: list[DocRuleInfo]
