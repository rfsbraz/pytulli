# generated by datamodel-codegen:
#   filename:  data.json
#   timestamp: 2021-01-27T05:08:21+00:00

from __future__ import annotations

from typing import Any, List, Optional

from pydantic import BaseModel


class Stream(BaseModel):
    id: Optional[str]
    type: Optional[str]
    video_codec: Optional[str] = None
    video_codec_level: Optional[str] = None
    video_bitrate: Optional[str] = None
    video_bit_depth: Optional[str] = None
    video_chroma_subsampling: Optional[str] = None
    video_color_primaries: Optional[str] = None
    video_color_range: Optional[str] = None
    video_color_space: Optional[str] = None
    video_color_trc: Optional[str] = None
    video_frame_rate: Optional[str] = None
    video_ref_frames: Optional[str] = None
    video_height: Optional[str] = None
    video_width: Optional[str] = None
    video_language: Optional[str] = None
    video_language_code: Optional[str] = None
    video_profile: Optional[str] = None
    video_scan_type: Optional[str] = None
    selected: Optional[int]
    audio_codec: Optional[str] = None
    audio_bitrate: Optional[str] = None
    audio_bitrate_mode: Optional[str] = None
    audio_channels: Optional[str] = None
    audio_channel_layout: Optional[str] = None
    audio_sample_rate: Optional[str] = None
    audio_language: Optional[str] = None
    audio_language_code: Optional[str] = None
    audio_profile: Optional[str] = None
    subtitle_codec: Optional[str] = None
    subtitle_container: Optional[str] = None
    subtitle_format: Optional[str] = None
    subtitle_forced: Optional[int] = None
    subtitle_location: Optional[str] = None
    subtitle_language: Optional[str] = None
    subtitle_language_code: Optional[str] = None


class Part(BaseModel):
    id: Optional[str]
    file: Optional[str]
    file_size: Optional[str]
    indexes: Optional[int]
    streams: Optional[List[Stream]]
    selected: Optional[int]


class MediaInfoItem(BaseModel):
    id: Optional[str]
    container: Optional[str]
    bitrate: Optional[str]
    height: Optional[str]
    width: Optional[str]
    aspect_ratio: Optional[str]
    video_codec: Optional[str]
    video_resolution: Optional[str]
    video_full_resolution: Optional[str]
    video_framerate: Optional[str]
    video_profile: Optional[str]
    audio_codec: Optional[str]
    audio_channels: Optional[str]
    audio_channel_layout: Optional[str]
    audio_profile: Optional[str]
    optimized_version: Optional[int]
    channel_call_sign: Optional[str]
    channel_identifier: Optional[str]
    channel_thumb: Optional[str]
    parts: Optional[List[Part]]


class MovieItem(BaseModel):
    media_type: Optional[str]
    section_id: Optional[str]
    library_name: Optional[str]
    rating_key: Optional[str]
    parent_rating_key: Optional[str]
    grandparent_rating_key: Optional[str]
    title: Optional[str]
    parent_title: Optional[str]
    grandparent_title: Optional[str]
    original_title: Optional[str]
    sort_title: Optional[str]
    media_index: Optional[str]
    parent_media_index: Optional[str]
    studio: Optional[str]
    content_rating: Optional[str]
    summary: Optional[str]
    tagline: Optional[str]
    rating: Optional[str]
    rating_image: Optional[str]
    audience_rating: Optional[str]
    audience_rating_image: Optional[str]
    user_rating: Optional[str]
    duration: Optional[str]
    year: Optional[str]
    thumb: Optional[str]
    parent_thumb: Optional[str]
    grandparent_thumb: Optional[str]
    art: Optional[str]
    banner: Optional[str]
    originally_available_at: Optional[str]
    added_at: Optional[str]
    updated_at: Optional[str]
    last_viewed_at: Optional[str]
    guid: Optional[str]
    parent_guid: Optional[str]
    grandparent_guid: Optional[str]
    directors: Optional[List]
    writers: Optional[List]
    actors: Optional[List]
    genres: Optional[List]
    labels: Optional[List]
    collections: Optional[List]
    guids: Optional[List]
    full_title: Optional[str]
    children_count: Optional[int]
    live: Optional[int]
    media_info: Optional[List[MediaInfoItem]]


class ShowItem(BaseModel):
    media_type: Optional[str]
    section_id: Optional[str]
    library_name: Optional[str]
    rating_key: Optional[str]
    parent_rating_key: Optional[str]
    grandparent_rating_key: Optional[str]
    title: Optional[str]
    parent_title: Optional[str]
    grandparent_title: Optional[str]
    original_title: Optional[str]
    sort_title: Optional[str]
    media_index: Optional[str]
    parent_media_index: Optional[str]
    studio: Optional[str]
    content_rating: Optional[str]
    summary: Optional[str]
    tagline: Optional[str]
    rating: Optional[str]
    rating_image: Optional[str]
    audience_rating: Optional[str]
    audience_rating_image: Optional[str]
    user_rating: Optional[str]
    duration: Optional[str]
    year: Optional[str]
    thumb: Optional[str]
    parent_thumb: Optional[str]
    grandparent_thumb: Optional[str]
    art: Optional[str]
    banner: Optional[str]
    originally_available_at: Optional[str]
    added_at: Optional[str]
    updated_at: Optional[str]
    last_viewed_at: Optional[str]
    guid: Optional[str]
    parent_guid: Optional[str]
    grandparent_guid: Optional[str]
    directors: Optional[List]
    writers: Optional[List]
    actors: Optional[List[str]]
    genres: Optional[List[str]]
    labels: Optional[List]
    collections: Optional[List]
    guids: Optional[List]
    full_title: Optional[str]
    children_count: Optional[int]
    live: Optional[int]
    media_info: Optional[List]


class SeasonItem(BaseModel):
    media_type: Optional[str]
    section_id: Optional[str]
    library_name: Optional[str]
    rating_key: Optional[str]
    parent_rating_key: Optional[str]
    grandparent_rating_key: Optional[str]
    title: Optional[str]
    parent_title: Optional[str]
    grandparent_title: Optional[str]
    original_title: Optional[str]
    sort_title: Optional[str]
    media_index: Optional[str]
    parent_media_index: Optional[str]
    studio: Optional[str]
    content_rating: Optional[str]
    summary: Optional[str]
    tagline: Optional[str]
    rating: Optional[str]
    rating_image: Optional[str]
    audience_rating: Optional[str]
    audience_rating_image: Optional[str]
    user_rating: Optional[str]
    duration: Optional[str]
    year: Optional[str]
    thumb: Optional[str]
    parent_thumb: Optional[str]
    grandparent_thumb: Optional[str]
    art: Optional[str]
    banner: Optional[str]
    originally_available_at: Optional[str]
    added_at: Optional[str]
    updated_at: Optional[str]
    last_viewed_at: Optional[str]
    guid: Optional[str]
    parent_guid: Optional[str]
    grandparent_guid: Optional[str]
    directors: Optional[List]
    writers: Optional[List]
    actors: Optional[List[str]]
    genres: Optional[List[str]]
    labels: Optional[List]
    collections: Optional[List]
    guids: Optional[List]
    full_title: Optional[str]
    children_count: Optional[int]
    live: Optional[int]
    media_info: Optional[List]


class EpisodeItem(BaseModel):
    media_type: Optional[str]
    section_id: Optional[str]
    library_name: Optional[str]
    rating_key: Optional[str]
    parent_rating_key: Optional[str]
    grandparent_rating_key: Optional[str]
    title: Optional[str]
    parent_title: Optional[str]
    grandparent_title: Optional[str]
    original_title: Optional[str]
    sort_title: Optional[str]
    media_index: Optional[str]
    parent_media_index: Optional[str]
    studio: Optional[str]
    content_rating: Optional[str]
    summary: Optional[str]
    tagline: Optional[str]
    rating: Optional[str]
    rating_image: Optional[str]
    audience_rating: Optional[str]
    audience_rating_image: Optional[str]
    user_rating: Optional[str]
    duration: Optional[str]
    year: Optional[str]
    thumb: Optional[str]
    parent_thumb: Optional[str]
    grandparent_thumb: Optional[str]
    art: Optional[str]
    banner: Optional[str]
    originally_available_at: Optional[str]
    added_at: Optional[str]
    updated_at: Optional[str]
    last_viewed_at: Optional[str]
    guid: Optional[str]
    parent_guid: Optional[str]
    grandparent_guid: Optional[str]
    directors: Optional[List[str]]
    writers: Optional[List[str]]
    actors: Optional[List[str]]
    genres: Optional[List[str]]
    labels: Optional[List]
    collections: Optional[List]
    guids: Optional[List]
    full_title: Optional[str]
    children_count: Optional[int]
    live: Optional[int]
    media_info: Optional[List[MediaInfoItem]]


class ResultsList(BaseModel):
    movie: Optional[List[MovieItem]]
    show: Optional[List[ShowItem]]
    season: Optional[List[SeasonItem]]
    episode: Optional[List[EpisodeItem]]
    artist: Optional[List]
    album: Optional[List]
    track: Optional[List]
    collection: Optional[List]


class Data(BaseModel):
    results_count: Optional[int]
    results_list: Optional[ResultsList]


class Response(BaseModel):
    result: Optional[str]
    message: Any
    data: Data


class Model(BaseModel):
    response: Response