# generated by datamodel-codegen:
#   filename:  data.json
#   timestamp: 2021-01-27T04:24:52+00:00

from __future__ import annotations

from typing import Any, List, Optional

from pydantic import BaseModel


class Datum(BaseModel):
    row_id: int
    user_id: int
    username: str
    friendly_name: str
    thumb: Optional[str]
    email: Optional[str]
    is_active: int
    is_admin: int
    is_home_user: Optional[int]
    is_allow_sync: Optional[int]
    is_restricted: Optional[int]
    do_notify: int
    keep_history: int
    allow_guest: int
    server_token: Optional[str]
    shared_libraries: Optional[str]
    filter_all: Optional[str]
    filter_movies: Optional[str]
    filter_tv: Optional[str]
    filter_music: Optional[str]
    filter_photos: Optional[str]


class Response(BaseModel):
    result: str
    message: Any
    data: List[Datum]


class Model(BaseModel):
    response: Response