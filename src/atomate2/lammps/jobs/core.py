import abc
from dataclasses import dataclass, field

from atomate2.lammps.common import (
    SimulationTimeStoppingCriteria,
    StoppingCriteria,
    Temperature,
    TemperatureProfile,
    Time,
)
from atomate2.lammps.jobs.base import BaseLammpsMaker
from atomate2.lammps.sets.base import BaseLammpsGenerator, LammpsMD, LammpsMinimization


@dataclass
class MDMaker(BaseLammpsMaker):
    name: str = "molecular dynamics"
    input_set_generator: BaseLammpsGenerator = field(default_factory=LammpsMD)
    stopping_criteria: str | StoppingCriteria = SimulationTimeStoppingCriteria(
        Time(5, "ps")
    )
    temperature: Temperature | TemperatureProfile = Temperature("1000 K")


@dataclass
class MinimizationMaker(BaseLammpsMaker):
    name: str = "minimization"
    input_set_generator: BaseLammpsGenerator = field(default_factory=LammpsMinimization)
