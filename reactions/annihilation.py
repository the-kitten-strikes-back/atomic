# atomic/reactions/annihilation.py

from atomic.particles.bosons import Photon
from atomic.particles.leptons import Electron, Positron
from atomic.reactions.base import NuclearReaction


class ElectronPositronAnnihilation(NuclearReaction):
    def __init__(self):
        super().__init__([Electron(), Positron()])

    def products(self):
        return [Photon(), Photon()]

    def _validate_quantum_numbers(self, products):
        charge_before = sum(r.qn.electric_charge for r in self.reactants)
        charge_after = sum(p.qn.electric_charge for p in products)
        if abs(charge_before - charge_after) > 1e-20:
            raise ValueError("Electric charge not conserved")

        lepton_before = sum(r.qn.lepton_number for r in self.reactants)
        lepton_after = sum(p.qn.lepton_number for p in products)
        if lepton_before != lepton_after:
            raise ValueError("Lepton number not conserved")

    def run(self):
        products = self.products()
        self._validate_quantum_numbers(products)
        self._last_energy_mev = self._estimate_energy_released(self.reactants, products)
        return products
