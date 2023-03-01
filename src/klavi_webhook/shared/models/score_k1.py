from dataclasses import dataclass, field
from marshmallow import Schema

import marshmallow_dataclass
import uuid

@dataclass
class ScoreK1:
    id: str = ""
    report_id: str = ""
    account_info: dict = field(default_factory=dict)
    score_detail: dict = field(default_factory=dict)

    def __post_init__(self):
        if self.id == "":
            self.id = uuid.uuid4()


ScoreK1Schema = marshmallow_dataclass.class_schema(ScoreK1)
