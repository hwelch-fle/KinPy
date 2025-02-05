# generated by datamodel-codegen:
#   filename:  CalcFieldForm
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
    unit: Optional[str] = None
    expression: Optional[str] = None
    code: Optional[str] = None
    format: Optional[
        Literal[
            'NUMBER',
            'NUMBER_DIGIT',
            'DATETIME',
            'DATE',
            'TIME',
            'HOUR_MINUTE',
            'DAY_HOUR_MINUTE',
        ]
    ] = None
    unitPosition: Optional[Literal['BEFORE', 'AFTER']] = None
    label: Optional[str] = None
    displayScale: Optional[str] = None
    hideExpression: Optional[bool] = None
    required: Optional[bool] = None
