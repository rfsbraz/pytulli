# generated by datamodel-codegen:
#   filename:  data.json
#   timestamp: 2021-01-27T01:23:27+00:00

from __future__ import annotations

from typing import Any, List, Optional

from pydantic import BaseModel
from tautulli import utils
from tautulli.models.activitysummary import ActivitySummary, build_summary_from_activity_object


class Session(BaseModel):
    session_key: str
    media_type: str
    view_offset: str
    progress_percent: str
    quality_profile: str
    synced_version_profile: str
    optimized_version_profile: str
    user: str
    channel_stream: int
    section_id: str
    library_name: str
    rating_key: str
    parent_rating_key: str
    grandparent_rating_key: str
    title: str
    parent_title: str
    grandparent_title: str
    original_title: str
    sort_title: str
    media_index: str
    parent_media_index: str
    studio: str
    content_rating: str
    summary: str
    tagline: str
    rating: str
    rating_image: str
    audience_rating: str
    audience_rating_image: str
    user_rating: str
    duration: str
    year: str
    thumb: str
    parent_thumb: str
    grandparent_thumb: str
    art: str
    banner: str
    originally_available_at: str
    added_at: str
    updated_at: str
    last_viewed_at: str
    guid: str
    parent_guid: str
    grandparent_guid: str
    directors: List
    writers: List
    actors: List
    genres: List[str]
    labels: List
    collections: List
    guids: List
    full_title: str
    children_count: int
    live: int
    id: str
    container: str
    bitrate: str
    height: str
    width: str
    aspect_ratio: str
    video_codec: str
    video_resolution: str
    video_full_resolution: str
    video_framerate: str
    video_profile: str
    audio_codec: str
    audio_channels: str
    audio_channel_layout: str
    audio_profile: str
    optimized_version: int
    channel_call_sign: str
    channel_identifier: str
    channel_thumb: str
    file: str
    file_size: str
    indexes: int
    selected: int
    type: str
    video_codec_level: str
    video_bitrate: str
    video_bit_depth: str
    video_chroma_subsampling: str
    video_color_primaries: str
    video_color_range: str
    video_color_space: str
    video_color_trc: str
    video_frame_rate: str
    video_ref_frames: str
    video_height: str
    video_width: str
    video_language: str
    video_language_code: str
    video_scan_type: str
    audio_bitrate: str
    audio_bitrate_mode: str
    audio_sample_rate: str
    audio_language: str
    audio_language_code: str
    subtitle_codec: str
    subtitle_container: str
    subtitle_format: str
    subtitle_forced: int
    subtitle_location: str
    subtitle_language: str
    subtitle_language_code: str
    row_id: int
    user_id: int
    username: str
    friendly_name: str
    user_thumb: str
    email: str
    is_active: int
    is_admin: int
    is_home_user: int
    is_allow_sync: int
    is_restricted: int
    do_notify: int
    keep_history: int
    deleted_user: int
    allow_guest: int
    shared_libraries: List[str]
    ip_address: str
    ip_address_public: str
    device: str
    platform: str
    platform_name: str
    platform_version: str
    product: str
    product_version: str
    profile: str
    player: str
    machine_id: str
    state: str
    local: int
    relayed: int
    secure: int
    session_id: str
    bandwidth: str
    location: str
    transcode_key: str
    transcode_throttled: int
    transcode_progress: int
    transcode_speed: str
    transcode_audio_channels: str
    transcode_audio_codec: str
    transcode_video_codec: str
    transcode_width: str
    transcode_height: str
    transcode_container: str
    transcode_protocol: str
    transcode_hw_requested: int
    transcode_hw_decode: str
    transcode_hw_decode_title: str
    transcode_hw_encode: str
    transcode_hw_encode_title: str
    transcode_hw_full_pipeline: int
    audio_decision: str
    video_decision: str
    subtitle_decision: str
    throttled: str
    transcode_hw_decoding: int
    transcode_hw_encoding: int
    stream_container: str
    stream_bitrate: str
    stream_aspect_ratio: str
    stream_audio_codec: str
    stream_audio_channels: str
    stream_audio_channel_layout: str
    stream_video_codec: str
    stream_video_framerate: str
    stream_video_resolution: str
    stream_video_height: str
    stream_video_width: str
    stream_duration: str
    stream_container_decision: str
    optimized_version_title: str
    synced_version: int
    live_uuid: str
    bif_thumb: str
    subtitles: int
    transcode_decision: str
    container_decision: str
    stream_video_full_resolution: Optional[str] = None
    video_dynamic_range: str
    stream_video_dynamic_range: str
    stream_video_bitrate: str
    stream_video_bit_depth: str
    stream_video_chroma_subsampling: str
    stream_video_color_primaries: str
    stream_video_color_range: str
    stream_video_color_space: str
    stream_video_color_trc: str
    stream_video_codec_level: str
    stream_video_ref_frames: str
    stream_video_language: str
    stream_video_language_code: str
    stream_video_scan_type: str
    stream_video_decision: str
    stream_audio_bitrate: str
    stream_audio_bitrate_mode: str
    stream_audio_sample_rate: str
    stream_audio_channel_layout_: str
    stream_audio_language: str
    stream_audio_language_code: str
    stream_audio_decision: str
    stream_subtitle_codec: str
    stream_subtitle_container: str
    stream_subtitle_format: str
    stream_subtitle_forced: int
    stream_subtitle_location: str
    stream_subtitle_language: str
    stream_subtitle_language_code: str
    stream_subtitle_decision: str
    stream_subtitle_transient: int

    @property
    def duration_milliseconds(self):
        try:
            return int(self.duration)
        except:
            return 0

    @property
    def location_milliseconds(self):
        try:
            return int(self.view_offset)
        except:
            return 0

    @property
    def progress_percentage(self):
        if not self.duration_milliseconds:
            return 0
        return int(self.location_milliseconds / self.duration_milliseconds)

    @property
    def progress_marker(self):
        if not self.location_milliseconds or not self.duration_milliseconds:
            return ""
        current_progress_min_sec = utils.milliseconds_to_minutes_seconds(milliseconds=self.location_milliseconds)
        total_min_sec = utils.milliseconds_to_minutes_seconds(milliseconds=self.duration_milliseconds)
        return f"{current_progress_min_sec}/{total_min_sec}"

    @property
    def eta(self):
        if not self.duration_milliseconds or not self.location_milliseconds:
            return ""
        milliseconds_remaining = self.duration_milliseconds - self.location_milliseconds
        eta_datetime = utils.now_plus_milliseconds(milliseconds=milliseconds_remaining)
        eta_string = utils.datetime_to_string(datetime_object=eta_datetime, string_format="%H:%M")
        return eta_string

    @property
    def status_icon(self):
        """
        Get icon for a stream state
        :return: emoji icon
        """
        return utils.switcher.get(self.state, "")

    @property
    def type_icon(self):
        if self.media_type in utils.media_type_icons:
            return utils.media_type_icons[self.media_type]
        # thanks twilsonco
        elif self.live:
            return utils.media_type_icons['live']
        return ""

    @property
    def human_bandwidth(self) -> str:
        try:
            return utils.human_bitrate(float(self.bandwidth))
        except:
            return utils.human_bitrate(0)

    @property
    def transcoding_stub(self):
        return ' (Transcode)' if self.stream_container_decision == 'transcode' else ''

    @property
    def summary(self) -> str:
        return f"{utils.session_title_message.format(icon=self.status_icon, username=self.username, media_type_icon=self.type_icon, title=self.title)}\n" \
               f"{utils.session_player_message.format(product=self.product, player=self.player)}\n" \
               f"{utils.session_details_message.format(quality_profile=self.quality_profile, bandwidth=self.human_bandwidth, transcoding=self.transcoding_stub)}\n" \
               f"{utils.session_progress_message.format(progress=self.progress_marker, eta=self.eta)}"


class Data(BaseModel):
    stream_count: str
    sessions: List[Session]
    stream_count_direct_play: int
    stream_count_direct_stream: int
    stream_count_transcode: int
    total_bandwidth: int
    lan_bandwidth: int
    wan_bandwidth: int

    @property
    def summary(self) -> ActivitySummary:
        return build_summary_from_activity_object(activity=self)


class Response(BaseModel):
    result: str
    message: Any
    data: Data


class Model(BaseModel):
    response: Response
