# atomic/particles/nuclei.py

from atomic.particles.hadrons import Proton, Neutron
from atomic.particles.base import Particle, QuantumNumbers

HELIUM4_MASS = 6.644657e-27  # kg

class Helium4Nucleus(Particle):
    def __init__(self):
        super().__init__(
            name="Helium-4 Nucleus",
            mass=HELIUM4_MASS,
            quantum_numbers=QuantumNumbers(
                electric_charge=2 * 1.602176634e-19,
                spin=0,
                baryon_number=4
            )
        )

        self.constituents = [
            Proton(), Proton(),
            Neutron(), Neutron()
        ]