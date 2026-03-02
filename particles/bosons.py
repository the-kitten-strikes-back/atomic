# atomic/particles/bosons.py

from .base import Particle, QuantumNumbers

E_CHARGE = 1.602176634e-19



class Photon(Particle):
    def __init__(self):
        super().__init__(
            name="Photon",
            mass=0.0,
            quantum_numbers=QuantumNumbers(
                electric_charge=0.0,
                spin=1
            ),
            lifetime=float("inf")
        )


class Gluon(Particle):
    def __init__(self, color, anticolor):
        super().__init__(
            name=f"Gluon ({color}-{anticolor})",
            mass=0.0,
            quantum_numbers=QuantumNumbers(
                electric_charge=0.0,
                spin=1,
                color_charge=f"{color}-{anticolor}"
            ),
            lifetime=float("inf")
        )



class WBosonPlus(Particle):
    def __init__(self):
        super().__init__(
            name="W+ Boson",
            mass=1.433e-25,  # kg (approx 80 GeV/c^2)
            quantum_numbers=QuantumNumbers(
                electric_charge=+E_CHARGE,
                spin=1
            ),
            lifetime=3e-25
        )


class WBosonMinus(Particle):
    def __init__(self):
        super().__init__(
            name="W- Boson",
            mass=1.433e-25,
            quantum_numbers=QuantumNumbers(
                electric_charge=-E_CHARGE,
                spin=1
            ),
            lifetime=3e-25
        )



class ZBoson(Particle):
    def __init__(self):
        super().__init__(
            name="Z Boson",
            mass=1.63e-25,  # kg (approx 91 GeV/c^2)
            quantum_numbers=QuantumNumbers(
                electric_charge=0.0,
                spin=1
            ),
            lifetime=3e-25
        )



class HiggsBoson(Particle):
    def __init__(self):
        super().__init__(
            name="Higgs Boson",
            mass=2.246e-25,  # kg (~125 GeV/c^2)
            quantum_numbers=QuantumNumbers(
                electric_charge=0.0,
                spin=0
            ),
            lifetime=1.6e-22
        )