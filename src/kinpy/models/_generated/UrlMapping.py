# generated by datamodel-codegen:
#   filename:  UrlMapping
#   timestamp: 2025-02-05T13:42:03+00:00

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal, Optional


@dataclass
class Model:
    destField: Optional[str] = None
    srcType: Optional[Literal['RECORD_URL']] = None
