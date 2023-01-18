from atomate2.lammps.common.conditions import Ensemble, TemperatureProfile
from atomate2.lammps.common.stopping_criteria import SimulationTimeStoppingCriteria


def test_minimization():

    from jobflow import run_locally
    from pymatgen.core import Element, Structure
    from pymatgen.transformations.advanced_transformations import (
        CubicSupercellTransformation,
    )

    from atomate2.lammps.jobs.core import MDMaker

    alo_structure = Structure(
        lattice=[[0, 2.13, 2.13], [2.13, 0, 2.13], [2.13, 2.13, 0]],
        species=["Al", "O"],
        coords=[[0, 0, 0], [0.5, 0.5, 0.5]],
    )

    alo_supercell = CubicSupercellTransformation(min_length=50).apply_transformation(
        alo_structure
    )

    maker = MDMaker(
        temperature=TemperatureProfile(temperature=300, end_temperature=3500, rate=10),
        stopping_criteria=SimulationTimeStoppingCriteria(
            simulation_time=100, equilibration_time=10
        ),
        ensemble=Ensemble("NPT"),
        pair_style="buck/coul/long 10",
        pair_coeff={
            ("Al", "Al"): (31570921.75, 0.068, 14.051),
            ("Al", "O"): (28476.906, 0.172, 34.578),
            ("O", "O"): (6462.67, 0.276, 85.092),
        },
        charges={"Al": 1.4175, "O": -0.945},
        masses={
            "Al": Element("Al").data["Atomic Mass"],
            "O": Element("O").data["Atomic Mass"],
        },
    )

    maker.make(
        input_structure=alo_supercell,
    )

    run_locally(job, create_folders=True)
