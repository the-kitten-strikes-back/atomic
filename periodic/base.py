# atomic/periodic/base.py

from dataclasses import dataclass
from typing import List, Optional, Type

from atomic.particles.hadrons import Proton, Neutron
from atomic.particles.leptons import Electron
from atomic.radiation.base import NuclearDecay


@dataclass
class AtomicStructure:
    protons: int
    neutrons: int
    electrons: int

    @property
    def mass_number(self):
        return self.protons + self.neutrons

    @property
    def atomic_number(self):
        return self.protons

    @property
    def is_ionized(self):
        return self.electrons != self.protons


class Element:
    name: str
    symbol: str

    def __init__(
        self,
        structure: AtomicStructure,
        radioactive: bool = False,
        decay_modes: Optional[List[Type[NuclearDecay]]] = None,
        half_life: Optional[float] = None,
        can_fission: bool = False,
        can_fuse: bool = True
    ):
        self.structure = structure
        self.radioactive = radioactive
        self.decay_modes = decay_modes or []
        self.half_life = half_life
        self.can_fission = can_fission
        self.can_fuse = can_fuse

    # ---------------------------
    # Nuclear Stability
    # ---------------------------

    def is_stable(self) -> bool:
        return not self.radioactive

    def neutron_proton_ratio(self) -> float:
        if self.structure.protons == 0:
            return 0
        return self.structure.neutrons / self.structure.protons

    # ---------------------------
    # Radiation Emission
    # ---------------------------

    def possible_decay_modes(self):
        return self.decay_modes

    def emits_radiation(self) -> bool:
        return self.radioactive

    # ---------------------------
    # Nuclear Reactions
    # ---------------------------

    def can_undergo_fission(self) -> bool:
        return self.can_fission

    def can_undergo_fusion(self) -> bool:
        return self.can_fuse

    # ---------------------------
    # Representation
    # ---------------------------

    def __repr__(self):
        return (
            f"{self.name} ({self.symbol}) | "
            f"Z={self.structure.atomic_number}, "
            f"A={self.structure.mass_number}"
        )