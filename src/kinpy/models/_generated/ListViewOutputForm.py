# generated by datamodel-codegen:
#   filename:  ListViewOutputForm
#   timestamp: 2025-02-05T13:42:03+00:00

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Literal, Optional


@dataclass
class Model:
    name: Optional[str] = None
    index: Optional[str] = None
    id: Optional[str] = None
    sort: Optional[str] = None
    fields: Optional[List[str]] = None
    type: Optional[Literal['LIST', 'CALENDAR', 'CUSTOM']] = None
    filterCond: Optional[str] = None
