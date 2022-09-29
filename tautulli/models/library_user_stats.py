# generated by datamodel-codegen:
#   filename:  data.json
#   timestamp: 2021-01-27T04:38:48+00:00

from __future__ import annotations

from typing import Any, List, Optional

from pydantic import BaseModel


class Datum(BaseModel):
    friendly_name: Optional[str]
    user_id: Optional[int]
    user_thumb: Optional[str]
    username: Optional[str]
    total_plays: Optional[int]


class Response(BaseModel):
    result: Optional[str]
    message: Any
    data: List[Datum]


class Model(BaseModel):
    response: Response