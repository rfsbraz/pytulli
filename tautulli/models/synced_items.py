# generated by datamodel-codegen:
#   filename:  data.json
#   timestamp: 2021-01-27T04:56:39+00:00

from __future__ import annotations

from typing import Any, List, Optional

from pydantic import BaseModel


class Datum(BaseModel):
    audio_bitrate: Optional[str]
    client_id: Optional[str]
    content_type: Optional[str]
    device_name: Optional[str]
    failure: Optional[str]
    item_complete_count: Optional[str]
    item_count: Optional[str]
    item_downloaded_count: Optional[str]
    item_downloaded_percent_complete: Optional[int]
    metadata_type: Optional[str]
    photo_quality: Optional[str]
    platform: Optional[str]
    rating_key: Optional[str]
    root_title: Optional[str]
    state: Optional[str]
    sync_id: Optional[str]
    sync_title: Optional[str]
    total_size: Optional[str]
    user: Optional[str]
    user_id: Optional[str]
    username: Optional[str]
    video_bitrate: Optional[str]
    video_quality: Optional[str]


class Response(BaseModel):
    result: Optional[str]
    message: Any
    data: List[Datum]


class Model(BaseModel):
    response: Response