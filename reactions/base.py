# atomic/reactions/base.py

class NuclearReaction:
    def __init__(self, reactants):
        self.reactants = reactants
        self._last_energy_mev = 0.0

    def products(self):
        raise NotImplementedError

    def energy_released(self):
        return self._last_energy_mev

    @staticmethod
    def _binding_energy_mev(structure):
        z = structure.protons
        n = structure.neutrons
        a = z + n
        if a <= 1:
            return 0.0

        a_v = 15.8
        a_s = 18.3
        a_c = 0.714
        a_a = 23.2
        a_p = 12.0

        pairing = 0.0
        if z % 2 == 0 and n % 2 == 0:
            pairing = a_p / (a ** 0.5)
        elif z % 2 == 1 and n % 2 == 1:
            pairing = -a_p / (a ** 0.5)

        return (
            a_v * a
            - a_s * (a ** (2.0 / 3.0))
            - a_c * (z * (z - 1)) / (a ** (1.0 / 3.0))
            - a_a * ((a - 2 * z) ** 2) / a
            + pairing
        )

    def _estimate_energy_released(self, reactants, products):
        be_reactants = sum(self._binding_energy_mev(r.structure) for r in reactants)
        be_products = sum(self._binding_energy_mev(p.structure) for p in products)
        return max(0.0, be_products - be_reactants)
