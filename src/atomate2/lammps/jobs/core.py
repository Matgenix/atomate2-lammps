from dataclasses import dataclass, field

from pymatgen.core import Structure

from atomate2.lammps.common import Ensemble, StoppingCriteria, TemperatureProfile
from atomate2.lammps.jobs.base import BaseLammpsMaker
from atomate2.lammps.sets.base import BaseLammpsGenerator, LammpsMD, LammpsMinimization

from ..files import write_lammps_input_set
from ..run import run_lammps
from ..schemas.task import TaskDocument
from ..sets.base import BaseLammpsGenerator


@dataclass
class MDMaker(BaseLammpsMaker):
    name: str = "molecular dynamics"
    input_set_generator: BaseLammpsGenerator = field(default_factory=LammpsMD)

    def make(
        self,
        input_structure: Structure,
        temperature: TemperatureProfile,
        stopping_criteria: StoppingCriteria,
        ensemble: Ensemble,
        pair_style: str,
        pair_coeff: dict[tuple[str, ...], tuple[float, ...]],
        charges: dict[str, float],
        masses: dict[str, float] = None,
        timestep: float = 0.01,
        kspace_style: str = "ewald 1.0e-6",
        units="metal",
        boundary="p p p",
        dimension=3,
        atom_style="charge",
        neighbor="3.0 bin",
        neigh_modify="every 1 check yes",
    ):
        write_lammps_input_set(
            input_structure, self.input_set_generator, **self.write_input_set_kwargs
        )

        for filename, data in self.write_additional_data.items():
            dumpfn(data, filename.replace(":", "."))

        run_lammps(**self.run_lammps_kwargs)

        task_doc = TaskDocument.from_directory(
            Path.cwd(), task_label=self.name, **self.task_document_kwargs
        )
        task_doc.task_label = self.name

        gzip_dir(".")

        return Response(output=task_doc)


@dataclass
class MinimizationMaker(BaseLammpsMaker):
    name: str = "minimization"
    input_set_generator: BaseLammpsGenerator = field(default_factory=LammpsMinimization)
