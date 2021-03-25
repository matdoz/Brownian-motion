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

# Particle stats
NUM_OF_PARTICLES = 100
PARTICLE_RADIUS = 10
PARTICLE_MASS = 1
PARTICLE_COLOR = (0, 0, 255)

# Molecule stats (the multiplier determines how much bigger in terms of radius and mass the molecule is compared to the particle)
MULTIPLIER = 5
MOLECULE_RADIUS = MULTIPLIER * PARTICLE_RADIUS
MOLECULE_MASS = MULTIPLIER * PARTICLE_MASS
MOLECULE_COLOR = (0, 0, 0)

# A boolean 2D grid for making sure particles don't spawn ontop of each other
GRID_X = int(WIDTH/(PARTICLE_RADIUS * 2 + 1))
GRID_Y = int(HEIGHT/(PARTICLE_RADIUS * 2 + 1))
GRID = ones((GRID_X, GRID_Y), dtype=bool)
