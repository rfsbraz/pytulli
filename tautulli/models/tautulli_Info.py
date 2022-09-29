# generated by datamodel-codegen:
#   filename:  data.json
#   timestamp: 2022-02-20T07:32:48+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel


class Data(BaseModel):
    tautulli_install_type: Optional[str]
    tautulli_version: Optional[str]
    tautulli_branch: Optional[str]
    tautulli_commit: Optional[str]
    tautulli_platform: Optional[str]
    tautulli_platform_release: Optional[str]
    tautulli_platform_version: Optional[str]
    tautulli_platform_linux_distro: Optional[str]
    tautulli_platform_device_name: Optional[str]
    tautulli_python_version: Optional[str]


class Model(BaseModel):
    result: Optional[str]
    message: Optional[str]
    data: Data