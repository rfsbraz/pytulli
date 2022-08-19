# generated by datamodel-codegen:
#   filename:  data.json
#   timestamp: 2021-01-27T04:34:08+00:00

from __future__ import annotations

from typing import Any

from pydantic import BaseModel


class Data(BaseModel):
    city: str
    code: str
    continent: str
    country: str
    latitude: float
    longitude: float
    postal_code: str
    region: str
    timezone: str
    accuracy: Any


class Response(BaseModel):
    result: str
    message: Any
    data: Data


class Model(BaseModel):
    response: Response
