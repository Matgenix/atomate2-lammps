from abc import ABC
from dataclasses import dataclass, field

from atomate2.lammps.common.units import Time

__all__ = (
    "StoppingCriteria",
    "SimulationTimeStoppingCriteria",
    "EquilibriumStoppingCriteria",
)


@dataclass
class StoppingCriteria(ABC):
    pass


class SimulationTimeStoppingCriteria(StoppingCriteria):
    """Stop the simulation after the amount of time has been simulated."""

    simulation_time: float = field(default_factory=Time)


class EquilibriumStoppingCriteria(StoppingCriteria):
    """Stop the simulation after equilibrium has been reached."""
