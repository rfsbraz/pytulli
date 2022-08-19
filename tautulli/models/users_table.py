# generated by datamodel-codegen:
#   filename:  data.json
#   timestamp: 2021-01-27T05:05:45+00:00

from __future__ import annotations

from typing import Any, List, Optional, Union

from pydantic import BaseModel


class Datum(BaseModel):
    row_id: int
    user_id: int
    username: str
    friendly_name: str
    user_thumb: str
    plays: int
    duration: int
    last_seen: Optional[int]
    last_played: Optional[str]
    history_row_id: Optional[int]
    ip_address: Optional[str]
    platform: Optional[str]
    player: Optional[str]
    rating_key: Optional[int]
    media_type: Optional[str]
    thumb: Optional[str]
    parent_title: Optional[str]
    year: Optional[int]
    media_index: Optional[Union[int, str]]
    parent_media_index: Optional[Union[int, str]]
    live: Optional[int]
    originally_available_at: Optional[str]
    guid: Optional[str]
    transcode_decision: Optional[str]
    do_notify: int
    keep_history: int
    allow_guest: int
    is_active: int
    title: str
    email: Optional[str]


class Data(BaseModel):
    recordsFiltered: int
    recordsTotal: int
    data: List[Datum]
    draw: int


class Response(BaseModel):
    result: str
    message: Any
    data: Data


class Model(BaseModel):
    response: Response
