# atomic/periodic/elements.py

from atomic.periodic.base import AtomicStructure, Element

# Keep imports resilient while radiation modules evolve.
try:
    from atomic.radiation.nucleardecay import AlphaDecay, BetaMinusDecay
except Exception:  # pragma: no cover
    try:
        from atomic.radiation.alpha import AlphaDecay
    except Exception:
        class AlphaDecay:  # type: ignore
            pass

    try:
        from atomic.radiation.beta import BetaMinusDecay
    except Exception:
        class BetaMinusDecay:  # type: ignore
            pass


SECONDS_PER_DAY = 24 * 3600
SECONDS_PER_YEAR = 365.25 * SECONDS_PER_DAY


class Hydrogen1(Element):
    name = "Hydrogen-1"
    symbol = "H"

    def __init__(self):
        super().__init__(
            structure=AtomicStructure(protons=1, neutrons=0, electrons=1),
            radioactive=False,
            can_fission=False,
            can_fuse=True,
        )


class Deuterium(Element):
    name = "Deuterium"
    symbol = "D"

    def __init__(self):
        super().__init__(
            structure=AtomicStructure(protons=1, neutrons=1, electrons=1),
            radioactive=False,
            can_fission=False,
            can_fuse=True,
        )


class Tritium(Element):
    name = "Tritium"
    symbol = "T"

    def __init__(self):
        super().__init__(
            structure=AtomicStructure(protons=1, neutrons=2, electrons=1),
            radioactive=True,
            decay_modes=[BetaMinusDecay],
            half_life=12.32 * SECONDS_PER_YEAR,
            can_fission=False,
            can_fuse=True,
        )


class Helium4(Element):
    name = "Helium-4"
    symbol = "He"

    def __init__(self):
        super().__init__(
            structure=AtomicStructure(protons=2, neutrons=2, electrons=2),
            radioactive=False,
            can_fission=False,
            can_fuse=True,
        )


class Carbon12(Element):
    name = "Carbon-12"
    symbol = "C"

    def __init__(self):
        super().__init__(
            structure=AtomicStructure(protons=6, neutrons=6, electrons=6),
            radioactive=False,
            can_fission=False,
            can_fuse=True,
        )


class Carbon14(Element):
    name = "Carbon-14"
    symbol = "C"

    def __init__(self):
        super().__init__(
            structure=AtomicStructure(protons=6, neutrons=8, electrons=6),
            radioactive=True,
            decay_modes=[BetaMinusDecay],
            half_life=5730 * SECONDS_PER_YEAR,
            can_fission=False,
            can_fuse=True,
        )


class Nitrogen14(Element):
    name = "Nitrogen-14"
    symbol = "N"

    def __init__(self):
        super().__init__(
            structure=AtomicStructure(protons=7, neutrons=7, electrons=7),
            radioactive=False,
            can_fission=False,
            can_fuse=True,
        )


class Oxygen16(Element):
    name = "Oxygen-16"
    symbol = "O"

    def __init__(self):
        super().__init__(
            structure=AtomicStructure(protons=8, neutrons=8, electrons=8),
            radioactive=False,
            can_fission=False,
            can_fuse=True,
        )


class Iron56(Element):
    name = "Iron-56"
    symbol = "Fe"

    def __init__(self):
        super().__init__(
            structure=AtomicStructure(protons=26, neutrons=30, electrons=26),
            radioactive=False,
            can_fission=False,
            can_fuse=False,
        )


class Cobalt60(Element):
    name = "Cobalt-60"
    symbol = "Co"

    def __init__(self):
        super().__init__(
            structure=AtomicStructure(protons=27, neutrons=33, electrons=27),
            radioactive=True,
            decay_modes=[BetaMinusDecay],
            half_life=5.2714 * SECONDS_PER_YEAR,
            can_fission=False,
            can_fuse=False,
        )


class Iodine131(Element):
    name = "Iodine-131"
    symbol = "I"

    def __init__(self):
        super().__init__(
            structure=AtomicStructure(protons=53, neutrons=78, electrons=53),
            radioactive=True,
            decay_modes=[BetaMinusDecay],
            half_life=8.02 * SECONDS_PER_DAY,
            can_fission=False,
            can_fuse=False,
        )


class Cesium137(Element):
    name = "Cesium-137"
    symbol = "Cs"

    def __init__(self):
        super().__init__(
            structure=AtomicStructure(protons=55, neutrons=82, electrons=55),
            radioactive=True,
            decay_modes=[BetaMinusDecay],
            half_life=30.17 * SECONDS_PER_YEAR,
            can_fission=False,
            can_fuse=False,
        )


class Thorium232(Element):
    name = "Thorium-232"
    symbol = "Th"

    def __init__(self):
        super().__init__(
            structure=AtomicStructure(protons=90, neutrons=142, electrons=90),
            radioactive=True,
            decay_modes=[AlphaDecay],
            half_life=1.405e10 * SECONDS_PER_YEAR,
            can_fission=False,
            can_fuse=False,
        )


class Uranium235(Element):
    name = "Uranium-235"
    symbol = "U"

    def __init__(self):
        super().__init__(
            structure=AtomicStructure(protons=92, neutrons=143, electrons=92),
            radioactive=True,
            decay_modes=[AlphaDecay],
            half_life=7.04e8 * SECONDS_PER_YEAR,
            can_fission=True,
            can_fuse=False,
        )


class Uranium238(Element):
    name = "Uranium-238"
    symbol = "U"

    def __init__(self):
        super().__init__(
            structure=AtomicStructure(protons=92, neutrons=146, electrons=92),
            radioactive=True,
            decay_modes=[AlphaDecay],
            half_life=4.468e9 * SECONDS_PER_YEAR,
            can_fission=False,
            can_fuse=False,
        )


class Radon222(Element):
    name = "Radon-222"
    symbol = "Rn"

    def __init__(self):
        super().__init__(
            structure=AtomicStructure(protons=86, neutrons=136, electrons=86),
            radioactive=True,
            decay_modes=[AlphaDecay],
            half_life=3.8235 * SECONDS_PER_DAY,
            can_fission=False,
            can_fuse=False,
        )


class Plutonium239(Element):
    name = "Plutonium-239"
    symbol = "Pu"

    def __init__(self):
        super().__init__(
            structure=AtomicStructure(protons=94, neutrons=145, electrons=94),
            radioactive=True,
            decay_modes=[AlphaDecay],
            half_life=24100 * SECONDS_PER_YEAR,
            can_fission=True,
            can_fuse=False,
        )


__all__ = [
    "Hydrogen1",
    "Deuterium",
    "Tritium",
    "Helium4",
    "Carbon12",
    "Carbon14",
    "Nitrogen14",
    "Oxygen16",
    "Iron56",
    "Cobalt60",
    "Iodine131",
    "Cesium137",
    "Thorium232",
    "Uranium235",
    "Uranium238",
    "Radon222",
    "Plutonium239",
]
