# atomic/radiation/base.py

class NuclearDecay:
    def __init__(self, parent):
        self.parent = parent

    def products(self):
        raise NotImplementedError

    def check_conservation(self, products):
        """
        Validates conservation of:
        - Electric charge
        - Baryon number
        - Lepton number
        """
        total_charge_before = self.parent.qn.electric_charge
        total_baryon_before = self.parent.qn.baryon_number
        total_lepton_before = self.parent.qn.lepton_number

        total_charge_after = sum(p.qn.electric_charge for p in products)
        total_baryon_after = sum(p.qn.baryon_number for p in products)
        total_lepton_after = sum(p.qn.lepton_number for p in products)

        return (
            abs(total_charge_before - total_charge_after) < 1e-20 and
            total_baryon_before == total_baryon_after and
            total_lepton_before == total_lepton_after
        )