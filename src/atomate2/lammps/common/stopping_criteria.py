from abc import ABC
from dataclasses import dataclass, field

__all__ = (
    "StoppingCriteria",
    "SimulationTimeStoppingCriteria",
    "EquilibriumStoppingCriteria",
)


@dataclass
class StoppingCriteria(ABC):
    ...


class SimulationTimeStoppingCriteria(StoppingCriteria):
    """Stop the simulation after a target amount of time has been simulated."""

    simulation_time: float = field(default_factory=float)
    """The simulation time to stop after, in ps."""

    equilibration_time: float = field(default_factory=float)
    """An initial period to use for equilibration in ps. Will not count towards
    the stopping criteria."""
