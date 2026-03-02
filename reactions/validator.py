# atomic/reactions/validator.py

class ReactionValidator:

    @staticmethod
    def total_mass_number(particles):
        return sum(p.structure.mass_number for p in particles)

    @staticmethod
    def total_atomic_number(particles):
        return sum(p.structure.atomic_number for p in particles)

    @classmethod
    def validate(cls, reactants, products):
        if cls.total_mass_number(reactants) != cls.total_mass_number(products):
            raise ValueError("Mass number not conserved")

        if cls.total_atomic_number(reactants) != cls.total_atomic_number(products):
            raise ValueError("Atomic number not conserved")

        return True