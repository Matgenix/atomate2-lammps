from dataclasses import dataclass, field

from jobflow import Flow, Maker
from pymatgen.core import Structure

from atomate2.lammps.common.units import Temperature, TemperatureProfile

from ..jobs.base import LammpsMaker
from ..jobs.core import MDMaker


@dataclass
class MeltQuenchThermalizeMaker(Maker):
    # potentially remove and replace with single job
    name: str = "melt-quench-thermalize"
    melt_maker: LammpsMaker = field(default_factory=MDMaker)
    quench_maker: LammpsMaker = field(default_factory=MDMaker)
    thermalize_maker: LammpsMaker = field(default_factory=MDMaker)

    def make(
        self,
        structure: Structure,
        melt_temperature: Temperature,
        thermalize_temperature: Temperature,
        quench_rate: float,
    ):
        melt = self.melt_maker.make(
            name="melt", structure=structure, temperature=melt_temperature
        )
        quench = self.quench_maker.make(
            name="quench",
            structure=melt.output.structure,
            temperature=TemperatureProfile(
                "linear",
                start=melt_temperature,
                end=thermalize_temperature,
                rate=quench_rate,
            ),
        )
        thermalize = self.thermalize_make.make(
            name="thermalize",
            structure=quench.output.structure,
            temperature=thermalize_temperature,
        )
        return Flow([melt, quench, thermalize], name=self.name)
