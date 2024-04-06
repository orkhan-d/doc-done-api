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

class DocRuleInfo(BaseModel):
    name: str

class DocRulesInfo(BaseModel):
    docrules: list[DocRuleInfo]