# atomic/reactions/fusion.py

from atomic.reactions.base import NuclearReaction
from atomic.reactions.validator import ReactionValidator
from atomic.periodic.base import AtomicStructure, Element
from atomic.periodic import elements as known_elements


class SynthesizedElement(Element):
    """Fallback element for isotopes not explicitly modeled in periodic.elements."""

    SYMBOLS = {
        1: "H", 2: "He", 3: "Li", 4: "Be", 5: "B", 6: "C", 7: "N", 8: "O",
        9: "F", 10: "Ne", 11: "Na", 12: "Mg", 13: "Al", 14: "Si", 15: "P",
        16: "S", 17: "Cl", 18: "Ar", 19: "K", 20: "Ca", 21: "Sc", 22: "Ti",
        23: "V", 24: "Cr", 25: "Mn", 26: "Fe", 27: "Co", 28: "Ni", 29: "Cu",
        30: "Zn",
    }

    def __init__(self, protons, neutrons):
        symbol = self.SYMBOLS.get(protons, f"E{protons}")
        mass_number = protons + neutrons
        self.name = f"{symbol}-{mass_number}"
        self.symbol = symbol
        super().__init__(
            structure=AtomicStructure(
                protons=protons,
                neutrons=neutrons,
                electrons=protons,
            ),
            radioactive=False,
            can_fission=False,
            can_fuse=True,
        )


class FusionReaction(NuclearReaction):
    def products(self):
        if len(self.reactants) < 2:
            raise ValueError("Fusion requires at least two reactants")

        for reactant in self.reactants:
            if not hasattr(reactant, "structure"):
                raise TypeError("All reactants must provide a .structure")
            if not getattr(reactant, "can_fuse", True):
                raise ValueError(f"{reactant} cannot undergo fusion")

        total_protons = sum(r.structure.protons for r in self.reactants)
        total_neutrons = sum(r.structure.neutrons for r in self.reactants)

        # Prefer explicit isotope classes when present.
        for element_name in getattr(known_elements, "__all__", []):
            element_cls = getattr(known_elements, element_name)
            element = element_cls()
            if (
                element.structure.protons == total_protons
                and element.structure.neutrons == total_neutrons
            ):
                return [element]

        return [SynthesizedElement(protons=total_protons, neutrons=total_neutrons)]

    def run(self):
        products = self.products()
        ReactionValidator.validate(self.reactants, products)
        self._last_energy_mev = self._estimate_energy_released(self.reactants, products)
        return products
