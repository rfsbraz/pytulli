# generated by datamodel-codegen:
#   filename:  data.json
#   timestamp: 2021-01-27T04:27:48+00:00

from __future__ import annotations

from typing import Any, List, Optional

from pydantic import BaseModel


class DatumModel(BaseModel):
    addedAt: Optional[str] = None
    art: Optional[Any] = None
    childCount: Optional[int] = None
    collectionMode: Optional[int] = None
    collectionSort: Optional[int] = None
    contentRating: Optional[str] = None
    guid: Optional[str] = None
    librarySectionID: Optional[str] = None
    librarySectionTitle: Optional[str] = None
    maxYear: Optional[int] = None
    minYear: Optional[int] = None
    ratingKey: Optional[int] = None
    subtype: Optional[str] = None
    summary: Optional[str] = None
    thumb: Optional[str] = None
    title: Optional[str] = None
    titleSort: Optional[str] = None
    type: Optional[str] = None
    updatedAt: Optional[str] = None


class CollectionsTableModel(BaseModel):
    recordsFiltered: Optional[int] = None
    recordsTotal: Optional[int] = None
    data: Optional[List[DatumModel]] = None
    draw: Optional[int] = None



