# generated by datamodel-codegen:
#   filename:  RequestForm
#   timestamp: 2025-02-05T13:42:03+00:00

from __future__ import annotations

from dataclasses import dataclass
from typing import Union

from . import (
    RecordAssigneesPutForm,
    RecordPostForm,
    RecordPutForm,
    RecordsDeleteForm,
    RecordsPostForm,
    RecordsPutForm,
    RecordsStatusPutForm,
    RecordStatusPutForm,
)


@dataclass
class Model:
    method: str
    payload: Union[
        RecordPostForm.Model,
        RecordPutForm.Model,
        RecordStatusPutForm.Model,
        RecordAssigneesPutForm.Model,
        RecordsDeleteForm.Model,
        RecordsPostForm.Model,
        RecordsPutForm.Model,
        RecordsStatusPutForm.Model,
    ]
    api: str
