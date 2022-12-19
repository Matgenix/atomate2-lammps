from dataclasses import dataclass, field

from atomate2.lammps.sets.base import BaseLammpsGenerator, LammpsMinimization

from ..jobs.base import BaseLammpsMaker


@dataclass
class MinimizationMaker(BaseLammpsMaker):
    name: str = "minimization"
    input_set_generator: BaseLammpsGenerator = field(default_factory=LammpsMinimization)
