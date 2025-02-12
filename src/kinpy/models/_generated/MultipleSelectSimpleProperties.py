# generated by datamodel-codegen:
#   filename:  MultipleSelectSimpleProperties
#   timestamp: 2025-02-05T13:42:03+00:00

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Literal, Optional


@dataclass
class Model:
    noLabel: Optional[str] = None
    code: Optional[str] = None
    defaultValue: Optional[List[str]] = None
    options: Optional[List[str]] = None
    label: Optional[str] = None
    type: Optional[
        Literal[
            'LABEL',
            'SPACER',
            'HR',
            'CREATED_TIME',
            'CREATOR',
            'DATE',
            'DATETIME',
            'NUMBER',
            'CALC',
            'RICH_TEXT',
            'FILE',
            'UPDATED_TIME',
            'MODIFIER',
            'CHECK_BOX',
            'MULTI_LINE_TEXT',
            'MULTI_SELECT',
            'RECORD_NUMBER',
            'RADIO_BUTTON',
            'SINGLE_LINE_TEXT',
            'DROP_DOWN',
            'SUBTABLE',
            'TIME',
            'USER_SELECT',
            'ORGANIZATION_SELECT',
            'GROUP_SELECT',
            'REFERENCE_TABLE',
            'LINK',
        ]
    ] = None
    required: Optional[str] = None
