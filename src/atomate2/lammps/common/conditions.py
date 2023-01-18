from dataclasses import dataclass, field
from enum import Enum, auto


class Ensembles(str, Enum):
    nvt = auto()
    npt = auto()
    nph = auto()


@dataclass
class TemperatureProfile:
    """This is used to defines temperature profiles during the simulation."""

    temperature: float = field(default_factory=float)
    """The target temperature at the start of the simulation, in Kelvin."""

    end_temperature: float | None = field(default_factory=float)
    """The target temperature at the end of the simulation, in Kelvin."""

    ramp_rate: float | None = field(default=10.0)
    """The target temperature ramp rate to apply between the initial and final
    temperatures, in Kelvin/ps."""


@dataclass
class Ensemble:

    style: Ensembles = field(default_factory=Ensembles)
