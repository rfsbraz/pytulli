# generated by datamodel-codegen:
#   filename:  data.json
#   timestamp: 2021-01-27T05:05:19+00:00

from __future__ import annotations

from typing import Any, List, Optional

from pydantic import BaseModel


class UserWatchTimeStats(BaseModel):
    query_days: Optional[int]
    total_plays: Optional[int]
    total_time: Optional[int]


class Response(BaseModel):
    result: Optional[str]
    message: Any
    data: List[UserWatchTimeStats]


class Model(BaseModel):
    response: Response
