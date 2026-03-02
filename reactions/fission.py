# atomic/reactions/fission.py

from atomic.reactions.base import NuclearReaction
from atomic.reactions.validator import ReactionValidator
from atomic.periodic import elements as known_elements
from atomic.reactions.fusion import SynthesizedElement


class FissionReaction(NuclearReaction):
    @staticmethod
    def _resolve_isotope(protons, neutrons):
        for element_name in getattr(known_elements, "__all__", []):
            element_cls = getattr(known_elements, element_name)
            element = element_cls()
            if (
                element.structure.protons == protons
                and element.structure.neutrons == neutrons
            ):
                return element
        return SynthesizedElement(protons=protons, neutrons=neutrons)

    def products(self):
        if len(self.reactants) != 1:
            raise ValueError("Fission expects exactly one parent nucleus")

        parent = self.reactants[0]
        if not hasattr(parent, "structure"):
            raise TypeError("Parent reactant must provide a .structure")
        if not getattr(parent, "can_fission", False):
            raise ValueError(f"{parent} cannot undergo fission")

        total_protons = parent.structure.protons
        total_neutrons = parent.structure.neutrons

        # Simple deterministic split into two daughter nuclei.
        daughter1_protons = total_protons // 2
        daughter2_protons = total_protons - daughter1_protons
        daughter1_neutrons = total_neutrons // 2
        daughter2_neutrons = total_neutrons - daughter1_neutrons

        daughter1 = self._resolve_isotope(daughter1_protons, daughter1_neutrons)
        daughter2 = self._resolve_isotope(daughter2_protons, daughter2_neutrons)
        return [daughter1, daughter2]

    def run(self):
        products = self.products()
        ReactionValidator.validate(self.reactants, products)
        self._last_energy_mev = self._estimate_energy_released(self.reactants, products)
        return products
