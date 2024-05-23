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

class ValueInfo(BaseModel):
    id: int
    value: str

class RuleInfo(BaseModel):
    id: int
    name: str
    definition: str | None
    type: str
    values: list[ValueInfo]

class RuleList(BaseModel):
    rules: list[RuleInfo]