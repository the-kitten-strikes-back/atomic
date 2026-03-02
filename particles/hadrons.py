# atomic/particles/hadrons.py

from .quarks import UpQuark, DownQuark
from .base import Particle, QuantumNumbers

PROTON_MASS = 1.6726219e-27
E_CHARGE = 1.602176634e-19
NEUTRON_MASS = 1.674927498e-27  # kg


class Neutron(Particle):
    def __init__(self):
        super().__init__(
            name="Neutron",
            mass=NEUTRON_MASS,
            quantum_numbers=QuantumNumbers(
                electric_charge=0.0,
                spin=0.5,
                baryon_number=1
            ),
            lifetime=880.2  # seconds (free neutron)
        )

        self.constituents = [
            UpQuark("red"),
            DownQuark("green"),
            DownQuark("blue")
        ]

    def decay_products(self):
        """
        Beta decay:
        n → p + e⁻ + ν̄_e
        """
        from .hadrons import Proton
        from .leptons import Electron, ElectronAntineutrino

        return [
            Proton(),
            Electron(),
            ElectronAntineutrino()
        ]
    
class Proton(Particle):
    def __init__(self):
        super().__init__(
            name="Proton",
            mass=PROTON_MASS,
            quantum_numbers=QuantumNumbers(
                electric_charge=+E_CHARGE,
                spin=0.5,
                baryon_number=1
            ),
            lifetime=float("inf")
        )

        self.constituents = [
            UpQuark("red"),
            UpQuark("green"),
            UpQuark("blue")
        ]