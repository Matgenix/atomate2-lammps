from pathlib import Path
from typing import Type

from pydantic import Field

from atomate2.common.schemas.structure import StructureMetadata


class TaskDocument(StructureMetadata):

    dir_name: str = Field()

    task_label: str = Field()

    @classmethod
    def from_directory(
        cls: Type["TaskDocument"],
        dir_name: str | Path,
        task_label: str,
    ) -> "TaskDocument":
        return TaskDocument(dir_name=str(dir_name), task_label=task_label)

    class Config:
        extras = "allow"
