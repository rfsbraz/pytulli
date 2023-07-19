# generated by datamodel-codegen:
#   filename:  data.json
#   timestamp: 2021-01-27T03:52:33+00:00

from __future__ import annotations

from typing import Any, Optional

from pydantic import BaseModel


class NewsletterNotification(BaseModel):
    newsletter_notification_id: Optional[int]


class Response(BaseModel):
    result: Optional[str]
    message: Any
    data: NewsletterNotification


class Model(BaseModel):
    response: Response