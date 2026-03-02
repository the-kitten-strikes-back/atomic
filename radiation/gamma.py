# atomic/radiation/gamma.py

from .base import NuclearDecay
from atomic.particles.bosons import Photon

class GammaDecay(NuclearDecay):
    def __init__(self, parent, energy):
        super().__init__(parent)
        self.energy = energy

    def products(self):
        photon = Photon()
        photon.emitted_energy = self.energy
        return [photon]