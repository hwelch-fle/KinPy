# generated by datamodel-codegen:
#   filename:  LabelField
#   timestamp: 2025-02-05T13:42:03+00:00

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal, Optional


@dataclass
class Size:
    width: Optional[str] = None


@dataclass
class Model:
    type: Literal[
        'CALC',
        'CHECK_BOX',
        'CREATED_TIME',
        'CREATOR',
        'DATE',
        'DATETIME',
        'DROP_DOWN',
        'FILE',
        'HR',
        'LABEL',
        'LINK',
        'MODIFIER',
        'MULTI_LINE_TEXT',
        'MULTI_SELECT',
        'NUMBER',
        'RADIO_BUTTON',
        'RECORD_NUMBER',
        'REFERENCE_TABLE',
        'RICH_TEXT',
        'SINGLE_LINE_TEXT',
        'SPACER',
        'TIME',
        'UPDATED_TIME',
        'USER_SELECT',
        'ORGANIZATION_SELECT',
        'GROUP_SELECT',
    ]
    size: Optional[Size] = None
    label: Optional[str] = None
