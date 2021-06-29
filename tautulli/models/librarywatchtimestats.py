# generated by datamodel-codegen:
#   filename:  data.json
#   timestamp: 2021-01-27T04:39:18+00:00

from __future__ import annotations

from typing import Any, List

from pydantic import BaseModel


class Datum(BaseModel):
    query_days: int
    total_time: int
    total_plays: int


class Response(BaseModel):
    result: str
    message: Any
    data: List[Datum]


class Model(BaseModel):
    response: Response