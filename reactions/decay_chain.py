# atomic/reactions/decay_chain.py

class DecayChain:

    def __init__(self, element):
        self.element = element
        self.chain = []

    def simulate(self, max_steps=10):
        current = self.element

        for _ in range(max_steps):
            if not current.radioactive:
                break

            decay_mode = current.decay_modes[0]
            decay = decay_mode(current)
            products = decay.products()

            # assume first nuclear product is new nucleus
            current = products[0]
            self.chain.append(current)

        return self.chain