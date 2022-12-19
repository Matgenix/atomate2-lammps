from pathlib import Path

from pymatgen.core import Structure
from pymatgen.io.lammps.sets import BaseLammpsGenerator


def write_lammps_input_set(
    structure: Structure,
    input_set_generator: BaseLammpsGenerator,
    directory: str | Path = ".",
    **kwargs,
):
    input_set = input_set_generator.get_input_set(structure)
    input_set.write_input(directory)
