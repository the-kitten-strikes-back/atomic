from atomic.reactions.fusion import FusionReaction
from atomic.periodic.base import Element, AtomicStructure


class Hydrogen1(Element):
    name = "Hydrogen-1"
    symbol = "H"

    def __init__(self):
        super().__init__(
            structure=AtomicStructure(
                protons=1,
                neutrons=0,
                electrons=1
            ),
            radioactive=False
        )


class Helium4(Element):
    name = "Helium-4"
    symbol = "He"

    def __init__(self):
        super().__init__(
            structure=AtomicStructure(
                protons=2,
                neutrons=2,
                electrons=2
            ),
            radioactive=False
        )


class ProtonProtonChain(FusionReaction):
    def __init__(self):
        super().__init__([
            Hydrogen1(),
            Hydrogen1(),
            Hydrogen1(),
            Hydrogen1()
        ])

    def products(self):
        return [Helium4()]

    def fuse(self, core, amount: float):
        hydrogen_available = core.composition.get("H", 0)
        max_reactions = hydrogen_available // 4

        if max_reactions <= 0:
            return 0.0

        reactions = min(max_reactions, amount // 4)

        if reactions <= 0:
            return 0.0

        core.composition["H"] -= reactions * 4
        core.composition["He"] = core.composition.get("He", 0) + reactions
        energy = reactions * 26.7

        return energy
