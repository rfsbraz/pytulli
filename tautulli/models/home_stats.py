# generated by datamodel-codegen:
#   filename:  data.json
#   timestamp: 2021-01-27T04:35:34+00:00

from __future__ import annotations

from typing import Any, List, Optional, Union

from pydantic import BaseModel


class Row(BaseModel):
    title: Optional[str]
    users_watched: Optional[Union[int, str]] = None
    rating_key: Optional[Union[int, str]] = None
    last_play: Optional[int] = None
    total_plays: Optional[int] = None
    grandparent_thumb: Optional[str] = None
    thumb: Optional[str] = None
    art: Optional[str] = None
    section_id: Optional[int] = None
    media_type: Optional[str] = None
    content_rating: Optional[str] = None
    labels: Optional[List] = None
    user: Optional[str] = None
    friendly_name: Optional[str] = None
    platform: Optional[str] = None
    live: Optional[int] = None
    guid: Optional[str] = None
    row_id: Optional[Union[int, str]] = None
    total_duration: Optional[int] = None
    count: Optional[int] = None
    started: Optional[str] = None
    stopped: Optional[str] = None
    user_id: Optional[int] = None
    user_thumb: Optional[str] = None
    platform_name: Optional[str] = None
    last_watch: Optional[int] = None
    player: Optional[str] = None


class Datum(BaseModel):
    stat_id: Optional[str]
    stat_title: Optional[str]
    rows: Optional[List[Row]]
    stat_type: Optional[str] = None


class Response(BaseModel):
    result: Optional[str]
    message: Any
    data: List[Datum]


class Model(BaseModel):
    response: Response