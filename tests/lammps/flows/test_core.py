import pytest


def test_minimization(mock_lammps, clean_dir, si_structure):

    from jobflow import run_locally

    from atomate2.lammps.jobs.core import MinimizationMaker

    job = MinimizationMaker.make()

    run_locally(job, create_folders=True)
