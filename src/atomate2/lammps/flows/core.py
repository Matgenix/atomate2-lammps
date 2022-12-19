from dataclasses import dataclass, field

from jobflow import Flow, Maker
from pymatgen.core import Structure

from atomate2.lammps.sets.base import BaseLammpsGenerator, LammpsMinimization

from ..jobs.base import LammpsMaker
from ..jobs.core import MinimizationMaker


@dataclass
class FMinimizationMaker(Maker):
    # potentially remove and replace with single job
    name: str = "minimization"
    minimization_maker: LammpsMaker = field(default_factory=MinimizationMaker)
    input_set_generator: BaseLammpsGenerator = field(default_factory=LammpsMinimization)

    def make(self, structure: Structure):
        return Flow([self.minimization_maker.make(structure)], name=self.name)
