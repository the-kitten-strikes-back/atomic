# atomic/particles/leptons.py

from .base import Particle, QuantumNumbers

E_CHARGE = 1.602176634e-19
ELECTRON_MASS = 9.10938356e-31

class Electron(Particle):
    def __init__(self):
        super().__init__(
            name="Electron",
            mass=ELECTRON_MASS,
            quantum_numbers=QuantumNumbers(
                electric_charge=-E_CHARGE,
                spin=0.5,
                lepton_number=1
            ),
            generation=1,
            antiparticle="Positron",
            magnetic_moment=-9.284764e-24,
            lifetime=float("inf")
        )


class Positron(Particle):
    def __init__(self):
        super().__init__(
            name="Positron",
            mass=ELECTRON_MASS,
            quantum_numbers=QuantumNumbers(
                electric_charge=+E_CHARGE,
                spin=0.5,
                lepton_number=-1
            ),
            generation=1,
            antiparticle="Electron",
            magnetic_moment=+9.284764e-24,
            lifetime=float("inf")
        )