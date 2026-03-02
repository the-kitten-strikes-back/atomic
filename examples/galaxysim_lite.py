# galaxy_sim_lite.py
import pygame
import numpy as np
from typing import List

from atomic.stellar.core import StellarCore
from atomic.stellar.burning import ProtonProtonChain

G = 0.1
WIDTH, HEIGHT = 1200, 800
CENTER = np.array([WIDTH / 2, HEIGHT / 2])


class GalaxySim:
    def __init__(self):
        self.positions = np.empty((0, 2), dtype=float)
        self.velocities = np.empty((0, 2), dtype=float)
        self.masses = np.array([], dtype=float)
        self.radii = np.array([], dtype=float)
        self.colors = []
        self.is_core = np.array([], dtype=bool)
        self.stars: List[StellarCore] = []

    def spawn_galaxy(self, center, n=300, core_mass=20000):
        angles = np.random.uniform(0, 2 * np.pi, n)
        distances = np.random.exponential(100, n)

        x = center[0] + distances * np.cos(angles)
        y = center[1] + distances * np.sin(angles)
        pos = np.column_stack((x, y))

        mass = np.random.uniform(5, 20, n)
        radius = np.clip(mass * 0.3, 1.5, 4)

        vel = np.zeros_like(pos)
        for i in range(n):
            r_vec = pos[i] - center
            r = np.linalg.norm(r_vec)
            if r == 0:
                continue
            speed = np.sqrt(G * core_mass / r)
            tangent = np.array([-r_vec[1], r_vec[0]]) / r
            vel[i] = tangent * speed

        # Core
        core_pos = np.array([[center[0], center[1]]])
        core_vel = np.array([[0.0, 0.0]])
        core_mass_arr = np.array([core_mass])
        core_radius = np.array([10.0])

        # Append arrays
        self.positions = np.vstack((self.positions, pos, core_pos))
        self.velocities = np.vstack((self.velocities, vel, core_vel))
        self.masses = np.concatenate((self.masses, mass, core_mass_arr))
        self.radii = np.concatenate((self.radii, radius, core_radius))
        self.is_core = np.concatenate(
            (self.is_core, np.zeros(n, dtype=bool), np.array([True]))
        )

        # Colors
        for _ in range(n):
            self.colors.append((255, 255, 200))
        self.colors.append((255, 215, 0))  # core

        # Create stellar cores
        for i in range(n):
            star = StellarCore(
                mass=float(mass[i]),
                temperature=15_000_000
            )
            self.stars.append(star)

        # Add core star
        core_star = StellarCore(
            mass=core_mass,
            temperature=20_000_000
        )
        self.stars.append(core_star)

    def _gravity_step(self, dt):
        n = len(self.masses)
        forces = np.zeros_like(self.positions)

        for i in range(n):
            for j in range(i + 1, n):
                r_vec = self.positions[j] - self.positions[i]
                dist = np.linalg.norm(r_vec) + 0.1
                force_mag = G * self.masses[i] * self.masses[j] / dist**2
                force = force_mag * r_vec / dist
                forces[i] += force
                forces[j] -= force

        self.velocities += forces / self.masses[:, None] * dt
        self.positions += self.velocities * dt

    def _stellar_step(self, dt):
        for i, star in enumerate(self.stars):
            if star.stage == "Dead":
                continue

            # Run fusion
            star.burn(ProtonProtonChain)

            self.radii[i] = star.radius
            self.masses[i] = star.mass

            # Update color by stage
            if star.stage == "main_sequence":
                self.colors[i] = (255, 255, 200)
            elif star.stage == "red_giant":
                self.colors[i] = (255, 120, 80)
            elif star.stage == "white_dwarf":
                self.colors[i] = (200, 220, 255)

    def _handle_collisions(self):
        i = 0
        while i < len(self.positions):
            j = i + 1
            while j < len(self.positions):
                dist = np.linalg.norm(self.positions[i] - self.positions[j])
                if dist < (self.radii[i] + self.radii[j]):

                    # Bigger mass wins
                    if self.masses[i] >= self.masses[j]:
                        winner, loser = i, j
                    else:
                        winner, loser = j, i

                    # Merge mass
                    self.masses[winner] += self.masses[loser]
                    self.radii[winner] *= 1.1

                    # Remove loser
                    self._remove_body(loser)
                    continue
                j += 1
            i += 1

    def _remove_body(self, index):
        self.positions = np.delete(self.positions, index, axis=0)
        self.velocities = np.delete(self.velocities, index, axis=0)
        self.masses = np.delete(self.masses, index)
        self.radii = np.delete(self.radii, index)
        self.is_core = np.delete(self.is_core, index)
        self.colors.pop(index)
        self.stars.pop(index)

    def step(self, dt):
        self._gravity_step(dt)
        self._handle_collisions()
        self._stellar_step(dt)

    def draw(self, screen):
        for i in range(len(self.positions)):
            pygame.draw.circle(
                screen,
                self.colors[i],
                np.nan_to_num(self.positions[i]).astype(int),
                int(self.radii[i])
            )


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    sim = GalaxySim()

    # Spawn two galaxies
    sim.spawn_galaxy(CENTER - np.array([200, 0]), 400)
    sim.spawn_galaxy(CENTER + np.array([200, 0]), 400)

    running = True
    while running:
        dt = clock.tick(60) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 20))

        sim.step(dt)
        sim.draw(screen)

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()