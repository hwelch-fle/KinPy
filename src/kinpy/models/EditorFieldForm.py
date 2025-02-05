# generated by datamodel-codegen:
#   filename:  EditorFieldForm
#   timestamp: 2025-02-05T13:42:03+00:00

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal, Optional


@dataclass
class Model:
    type: Literal[
        'CALC',
        'CATEGORY',
        'CHECK_BOX',
        'CREATED_TIME',
        'CREATOR',
        'DATE',
        'DATETIME',
        'DROP_DOWN',
        'FILE',
        'GROUP',
        'GROUP_SELECT',
        'LINK',
        'MODIFIER',
        'MULTI_LINE_TEXT',
        'MULTI_SELECT',
        'NUMBER',
        'ORGANIZATION_SELECT',
        'RADIO_BUTTON',
        'RECORD_NUMBER',
        'REFERENCE_TABLE',
        'RICH_TEXT',
        'SINGLE_LINE_TEXT',
        'STATUS',
        'STATUS_ASSIGNEE',
        'SUBTABLE',
        'TIME',
        'UPDATED_TIME',
        'USER_SELECT',
    ]
    noLabel: Optional[bool] = None
    code: Optional[str] = None
    defaultValue: Optional[str] = None
    label: Optional[str] = None
    required: Optional[bool] = None
