from typing import TypeAlias

from pint import Quantity


class PintType(str):
    Q = Quantity

    def __init__(self, dimensions: str):
        self._dimensions = dimensions

    @classmethod
    def validate(self, v):
        q = self.Q(v)
        if not q.check(self._dimensions):
            raise ValueError(
                "Value {v} must have dimensions of mass, not {v.dimensions}"
            )
        return q


Time: TypeAlias = PintType("[time]")
Temperature: TypeAlias = PintType("[temperature]")
