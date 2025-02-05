# generated by datamodel-codegen:
#   filename:  DecimalSimpleValue
#   timestamp: 2025-02-05T13:42:03+00:00

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal, Optional


@dataclass
class Model:
    type: Optional[
        Literal[
            'CATEGORY',
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
            'STATUS',
            'STATUS_ASSIGNEE',
            'SUBTABLE',
            'TIME',
            'USER_SELECT',
            'ORGANIZATION_SELECT',
            'GROUP_SELECT',
            'LINK',
            '__REVISION__',
            '__ID__',
        ]
    ] = None
    value: Optional[str] = None
