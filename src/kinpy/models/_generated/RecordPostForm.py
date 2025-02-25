# generated by datamodel-codegen:
#   filename:  RecordPostForm
#   timestamp: 2025-02-05T13:42:03+00:00

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Union

from . import (
    CalcSimpleValue,
    CategorySimpleValue,
    DateSimpleValue,
    DatetimeSimpleValue,
    DecimalSimpleValue,
    EditorSimpleValue,
    FileSimpleValue,
    GroupSelectSimpleValue,
    GroupSimpleValue,
    LinkSimpleValue,
    ModifiedAtSimpleValue,
    ModifierSimpleValue,
    MultipleLineTextSimpleValue,
    MultipleSelectSimpleValue,
    OrganizationSelectSimpleValue,
    RawRecordIdSimpleValue,
    RecordIdSimpleValue,
    ReferenceTableSimpleValue,
    RevisionSimpleValue,
    SimpleTableValue,
    SingleLineTextSimpleValue,
    SingleSelectSimpleValue,
    StatusSimpleValue,
    TimeSimpleValue,
    UserSelectSimpleValue,
)


@dataclass
class Model:
    app: str
    record: Dict[
        str,
        Union[
            CalcSimpleValue.Model,
            CategorySimpleValue.Model,
            DateSimpleValue.Model,
            DatetimeSimpleValue.Model,
            DecimalSimpleValue.Model,
            EditorSimpleValue.Model,
            FileSimpleValue.Model,
            GroupSimpleValue.Model,
            LinkSimpleValue.Model,
            ModifiedAtSimpleValue.Model,
            ModifierSimpleValue.Model,
            MultipleLineTextSimpleValue.Model,
            MultipleSelectSimpleValue.Model,
            RecordIdSimpleValue.Model,
            ReferenceTableSimpleValue.Model,
            SimpleTableValue.Model,
            SingleLineTextSimpleValue.Model,
            SingleSelectSimpleValue.Model,
            StatusSimpleValue.Model,
            TimeSimpleValue.Model,
            UserSelectSimpleValue.Model,
            OrganizationSelectSimpleValue.Model,
            GroupSelectSimpleValue.Model,
            RevisionSimpleValue.Model,
            RawRecordIdSimpleValue.Model,
        ],
    ]
