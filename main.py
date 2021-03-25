from setup import *
from particle import Particle
from collisionSystem import CollisionSystem


def instantiateMolecule(particles):
    g_x = int(GRID_X/2)
    g_y = int(GRID_Y/2)
    p_x = g_x * PARTICLE_RADIUS * 2 + PARTICLE_RADIUS
    p_y = g_y * PARTICLE_RADIUS * 2 + PARTICLE_RADIUS
    first_x_idx = g_x - int(MULTIPLIER/2)
    first_y_idx = g_y - int(MULTIPLIER/2)
    position = pygame.Vector2(p_x, p_y)
    velocity = pygame.Vector2(0, 0)
    particles.append(Particle(position,
                              velocity, MOLECULE_RADIUS, MOLECULE_MASS, MOLECULE_COLOR))

    # Occupying a square in the center of the grid where the molecule spawns
    for i in range(MULTIPLIER + 1):
        for j in range(MULTIPLIER + 1):
            GRID[first_x_idx + i][first_y_idx + j] = False


def instantiateParticle(particles, color=PARTICLE_COLOR, position=None, velocity=None):
    if position == None:
        g_x = randint(0, GRID_X)
        g_y = randint(0, GRID_Y)
    else:
        g_x = int(position.x)
        g_y = int(position.y)

    if velocity == None:
        v_x = uniform(-1, 1)
        v_y = uniform(-1, 1)
        velocity = pygame.Vector2(v_x, v_y)

    if GRID[g_x][g_y]:
        p_x = g_x * PARTICLE_RADIUS * 2 + PARTICLE_RADIUS
        p_y = g_y * PARTICLE_RADIUS * 2 + PARTICLE_RADIUS
        GRID[g_x][g_y] = False
        position = pygame.Vector2(p_x, p_y)
        particles.append(Particle(position, velocity,
                                  PARTICLE_RADIUS, PARTICLE_MASS, color))
        return

    else:
        for i in range(len(GRID)):
            for j in range(len(GRID[i])):
                if GRID[i][j]:
                    p_x = i * PARTICLE_RADIUS * 2 + PARTICLE_RADIUS
                    p_y = j * PARTICLE_RADIUS * 2 + PARTICLE_RADIUS
                    GRID[i][j] = False
                    position = pygame.Vector2(p_x, p_y)
                    particles.append(
                        Particle(position, velocity, PARTICLE_RADIUS, PARTICLE_MASS, color))
                    return
    print('The grid is full, too many particles instantiated.')


def main():
    # List of all the particles and the molecule
    particles = []

    # Instantiate the molecule and the particles
    instantiateMolecule(particles)
    for i in range(NUM_OF_PARTICLES):
        instantiateParticle(particles, PARTICLE_COLOR, None)

    CollisionSystem(particles).simulate()
    quit()


if __name__ == "__main__":
    main()
