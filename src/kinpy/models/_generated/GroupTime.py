# generated by datamodel-codegen:
#   filename:  GroupTime
#   timestamp: 2025-02-05T13:42:03+00:00

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal, Optional


@dataclass
class Model:
    code: Optional[str] = None
    per: Optional[Literal['HOUR', 'MINUTE']] = None
