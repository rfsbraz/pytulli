# generated by datamodel-codegen:
#   filename:  data.json
#   timestamp: 2022-08-26T22:20:41+00:00

from __future__ import annotations

from typing import Any, List, Optional

from pydantic import BaseModel


class MetadataField(BaseModel):
    field: Optional[str]
    level: Optional[int]


class MediaInfoField(BaseModel):
    field: Optional[str]
    level: Optional[int]


class Data(BaseModel):
    metadata_fields: Optional[List[MetadataField]]
    media_info_fields: Optional[List[MediaInfoField]]


class Response(BaseModel):
    result: str
    message: Any
    data: Data


class Model(BaseModel):
    response: Response