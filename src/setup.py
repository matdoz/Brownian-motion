import pygame
from numpy.random import uniform, randint
from numpy import ones, Inf, sqrt
from heapq import heappush, heappop
from time import sleep

# Constants for declaring the window where the simulation is running
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
BACKGROUND_COLOR = (255, 255, 255)
pygame.display.set_caption("Brownian motion")

# Molecule stats
NUM_OF_MOLECULES = 100
MOLECULE_RADIUS = 10
MOLECULE_MASS = 1
MOLECULE_COLOR = (0, 0, 255)

# Particle stats (the multiplier determines how much bigger in terms of radius and mass the particle is compared to the molecules)
MULTIPLIER = 5
PARTICLE_RADIUS = MULTIPLIER * MOLECULE_RADIUS
PARTICLE_MASS = MULTIPLIER * MOLECULE_MASS
PARTICLE_COLOR = (0, 0, 0)

# A boolean 2D grid for making sure molecules don't spawn ontop of each other when they are instantiated
GRID_X = int(WIDTH/(MOLECULE_RADIUS * 2 + 1))
GRID_Y = int(HEIGHT/(MOLECULE_RADIUS * 2 + 1))
GRID = ones((GRID_X, GRID_Y), dtype=bool)
