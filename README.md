# atomate2-lammps

This is an add-on package for [atomate2](https://github.com/materialsproject/atomate2) that includes core workflows for the [LAMMPS](https://lammps.org) molecular dynamics simulator.

## License

This add-on is released under the same license as atomate2, modified BSD, the
full text of which can be found in this repository.

## Status

This package is still under development and the API may change at any time.

## Quick start

```python
from atomate2.lammps.jobs.core import MDMaker
from jobflow import run_locally
from pymatgen.core import Structure
from pymatgen.transformations.advanced_transformations import
CubicSupercellTransformation

mgo_structure = Structure(
    lattice=[[0, 2.13, 2.13], [2.13, 0, 2.13], [2.13, 2.13, 0]],
    species=["Mg", "O"],
    coords=[[0, 0, 0], [0.5, 0.5, 0.5]],
)

mgo_supercell = CubicSupercellTransformation(min_length=50).apply_transformation(mgo_structure)

# melt supercell
MDMaker().make(mgo_supercell, temperature=1000)
```
