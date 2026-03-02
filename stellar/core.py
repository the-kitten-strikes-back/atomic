# atomic/stellar/core.py

class StellarCore:

    def __init__(self, mass: float, temperature: float):
        self.mass = mass
        self.temperature = temperature

        # Stellar properties
        self.radius = self._initial_radius()
        self.stage = "main_sequence"

        # Fuel (fraction of mass as hydrogen)
        self.hydrogen_fraction = 0.7
        self.helium_fraction = 0.28

    # ----------------------------
    # Internal Helpers
    # ----------------------------

    def _initial_radius(self):
        # Rough scaling: R ~ M^0.8
        return (self.mass / 1e30) ** 0.8 * 3

    # ----------------------------
    # Fusion
    # ----------------------------

    def burn(self, reaction_type):

        if self.hydrogen_fraction <= 0:
            self._evolve_off_main_sequence()
            return

        # Simple hydrogen consumption
        burn_rate = 1e-5  # tweak for speed

        self.hydrogen_fraction -= burn_rate
        self.helium_fraction += burn_rate

        # Very small mass loss via E=mc^2 approximation
        self.mass *= (1 - burn_rate * 0.0001)

        # Radius increases slowly
        self.radius *= (1 + burn_rate * 0.5)

        if self.hydrogen_fraction <= 0.1:
            self._evolve_off_main_sequence()

    # ----------------------------
    # Evolution
    # ----------------------------

    def _evolve_off_main_sequence(self):
        if self.stage == "main_sequence":
            self.stage = "red_giant"
            self.radius *= 5
            self.temperature *= 0.8