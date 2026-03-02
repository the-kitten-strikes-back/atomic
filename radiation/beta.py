# atomic/radiation/beta.py

from .base import NuclearDecay
from atomic.particles.hadrons import Proton, Neutron
from atomic.particles.leptons import (
    Electron,
    ElectronAntineutrino,
    Positron,
    ElectronNeutrino,
)

class BetaMinusDecay(NuclearDecay):
    def products(self):
        return [
            Proton(),
            Electron(),
            ElectronAntineutrino()
        ]


class BetaPlusDecay(NuclearDecay):
    def products(self):
        return [
            Neutron(),
            Positron(),
            ElectronNeutrino()
        ]