from atomic.reactions.annihilation import ElectronPositronAnnihilation


def main():
    reaction = ElectronPositronAnnihilation()

    print("Initial state:")
    for r in reaction.reactants:
        print(f"- {r}")

    products = reaction.run()

    print("\nReaction complete!")
    print(f"Products: {products}")
    print(f"Energy released: {reaction.energy_released():.6f} MeV")


if __name__ == "__main__":
    main()
