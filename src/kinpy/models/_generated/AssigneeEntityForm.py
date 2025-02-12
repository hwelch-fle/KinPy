# generated by datamodel-codegen:
#   filename:  AssigneeEntityForm
#   timestamp: 2025-02-05T13:42:03+00:00

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal, Optional


@dataclass
class Entity:
    code: Optional[str] = None
    type: Optional[
        Literal[
            'USER', 'GROUP', 'ORGANIZATION', 'FIELD_ENTITY', 'CREATOR', 'CUSTOM_FIELD'
        ]
    ] = None


@dataclass
class Model:
    includeSubs: Optional[bool] = None
    entity: Optional[Entity] = None
