# atomic/particles/base.py

from dataclasses import dataclass
from typing import Optional, List

C = 299_792_458  # m/s


@dataclass(frozen=True)
class QuantumNumbers:
    electric_charge: float
    spin: float
    baryon_number: float = 0
    lepton_number: float = 0
    isospin: Optional[float] = None
    hypercharge: Optional[float] = None
    color_charge: Optional[str] = None  # 'red', 'green', 'blue' or None


class Particle:
    def __init__(
        self,
        name: str,
        mass: float,
        quantum_numbers: QuantumNumbers,
        generation: Optional[int] = None,
        antiparticle: Optional[str] = None,
        magnetic_moment: Optional[float] = None,
        lifetime: Optional[float] = None,  # seconds
    ):
        self.name = name
        self.mass = mass
        self.qn = quantum_numbers
        self.generation = generation
        self.antiparticle = antiparticle
        self.magnetic_moment = magnetic_moment
        self.lifetime = lifetime

        # Dynamic state
        self.position = None
        self.momentum = None
        self.spin_state = None

    # ---------------------
    # Derived physics
    # ---------------------

    @property
    def rest_energy(self):
        return self.mass * C**2

    @property
    def statistics(self):
        return "fermion" if self.qn.spin % 1 != 0 else "boson"

    def info(self):
        return {
            "name": self.name,
            "mass (kg)": self.mass,
            "rest_energy (J)": self.rest_energy,
            "quantum_numbers": self.qn,
            "generation": self.generation,
            "magnetic_moment": self.magnetic_moment,
            "lifetime (s)": self.lifetime,
        }

    def __repr__(self):
        return f"<Particle: {self.name}>"