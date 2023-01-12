from pathlib import Path

import pytest

_REF_PATHS: dict[str, Path] = {}

from atomate2.lammps.sets.base import BaseLammpsGenerator


@pytest.fixture(scope="session")
def lammps_test_dir(test_dir):
    return test_dir / "lammps"


@pytest.fixture(scope="function")
def mock_lammps(monkeypatch, lammps_test_dir):
    def mock_run_lammps(*args, **kwargs):

        from jobflow import CURRENT_JOB

        name = CURRENT_JOB.job.name
        ref_path = lammps_test_dir / _REF_PATHS[name]

        fake_run_lammps(ref_path, **_FAKE_RUN_LAMMPS_KWARGS.get(name, {}))

    get_input_set_orig = BaseLammpsGenerator.get_input_set

    def mock_get_input_set(self, *args, **kwargs):
        return get_input_set_orig(self, *args, **kwargs)

    monkeypatch.setattr(atomate2.lammps.run, "run_lammps", mock_run_lammps)

    def _run(ref_paths, fake_run_lammps_kwargs=None):
        if fake_run_lammps_kwargs is None:
            fake_run_lammps_kwargs = {}

        _REF_PATHS.update(ref_paths)
        _FAKE_RUN_LAMMPS_KWARGS.update(fake_run_lammps_kwargs)

    yield _run

    monkeypatch.undo()
    _REF_PATHS.clear()
    _FAKE_RUN_LAMMPS_KWARGS.clear()


def fake_run_lammps(ref_path, settings):
    pass
