# generated by datamodel-codegen:
#   filename:  UserEntitySimpleValue
#   timestamp: 2025-02-05T13:42:03+00:00

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass
class Model:
    code: str
    name: Optional[str] = None
