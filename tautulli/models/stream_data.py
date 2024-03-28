# generated by datamodel-codegen:
#   filename:  data.json
#   timestamp: 2021-01-27T04:54:28+00:00

from __future__ import annotations

from typing import Any, Optional

from pydantic import BaseModel


class StreamDataModel(BaseModel):
    bitrate: Optional[int] = None
    video_full_resolution: Optional[str] = None
    optimized_version: Optional[str] = None
    optimized_version_profile: Optional[str] = None
    optimized_version_title: Optional[str] = None
    synced_version: Optional[str] = None
    synced_version_profile: Optional[str] = None
    container: Optional[str] = None
    video_codec: Optional[str] = None
    video_bitrate: Optional[int] = None
    video_width: Optional[int] = None
    video_height: Optional[int] = None
    video_framerate: Optional[str] = None
    video_dynamic_range: Optional[str] = None
    aspect_ratio: Optional[str] = None
    audio_codec: Optional[str] = None
    audio_bitrate: Optional[int] = None
    audio_channels: Optional[int] = None
    subtitle_codec: Optional[str] = None
    stream_bitrate: Optional[int] = None
    stream_video_full_resolution: Optional[str] = None
    quality_profile: Optional[str] = None
    stream_container_decision: Optional[str] = None
    stream_container: Optional[str] = None
    stream_video_decision: Optional[str] = None
    stream_video_codec: Optional[str] = None
    stream_video_bitrate: Optional[int] = None
    stream_video_width: Optional[int] = None
    stream_video_height: Optional[int] = None
    stream_video_framerate: Optional[str] = None
    stream_video_dynamic_range: Optional[str] = None
    stream_audio_decision: Optional[str] = None
    stream_audio_codec: Optional[str] = None
    stream_audio_bitrate: Optional[int] = None
    stream_audio_channels: Optional[int] = None
    subtitles: Optional[str] = None
    stream_subtitle_decision: Optional[str] = None
    stream_subtitle_codec: Optional[str] = None
    transcode_hw_decoding: Optional[str] = None
    transcode_hw_encoding: Optional[str] = None
    video_decision: Optional[str] = None
    audio_decision: Optional[str] = None
    media_type: Optional[str] = None
    title: Optional[str] = None
    grandparent_title: Optional[str] = None
    original_title: Optional[str] = None
    current_session: Optional[int] = None
    pre_tautulli: Optional[str] = None



