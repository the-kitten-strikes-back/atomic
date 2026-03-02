# atomic/particles/quarks.py

from .base import Particle, QuantumNumbers

UP_QUARK_MASS = 2.2e-30  # kg, simplified
DOWN_QUARK_MASS = 4.7e-30  # kg, simplified
E_CHARGE = 1.602176634e-19  # Coulombs

class UpQuark(Particle):
    def __init__(self, color="red"):
        super().__init__(
            name=f"Up Quark ({color})",
            mass=UP_QUARK_MASS,
            quantum_numbers=QuantumNumbers(
                electric_charge=+2/3 * E_CHARGE,
                spin=0.5,
                baryon_number=1/3,
                color_charge=color
            ),
            generation=1,
            antiparticle="Anti-Up Quark"
        )

class DownQuark(Particle):
    def __init__(self, color="red"):
        super().__init__(
            name=f"Down Quark ({color})",
            mass=DOWN_QUARK_MASS,
            quantum_numbers=QuantumNumbers(
                electric_charge=-1/3 * E_CHARGE,
                spin=0.5,
                baryon_number=1/3,
                color_charge=color
            ),
            generation=1,
            antiparticle="Anti-Down Quark"
        )