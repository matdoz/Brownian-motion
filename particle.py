from setup import pygame, WIN, Inf, sqrt, HEIGHT, WIDTH


class Particle:
    def __init__(self, position, velocity, radius, mass, color):
        self.p = position
        self.v = velocity
        self.radius = radius
        self.mass = mass
        self.color = color
        self.count = 0

    def move(self, dt):
        self.p.x += self.v.x * dt
        self.p.y += self.v.y * dt

    def draw(self):
        pygame.draw.circle(WIN, self.color, self.p, self.radius)

    def particle_collision_time(self, particle):
        if self == particle:
            return Inf
        dx, dy = particle.p.x - self.p.x, particle.p.y - self.p.y
        dvx, dvy = particle.v.x - self.v.x, particle.v.y - self.v.y
        dvdr = dx * dvx + dy * dvy
        if dvdr > 0:
            return Inf
        dvdv = dvx * dvx + dvy * dvy
        drdr = dx * dx + dy * dy
        sigma = self.radius + particle.radius
        d = (dvdr * dvdr) - dvdv * (drdr - sigma * sigma)
        if d <= 0:
            return Inf
        return - (dvdr + sqrt(d))/dvdv

    def vertical_wall_collision_time(self):
        if self.v.x > 0:
            return (WIDTH - self.p.x - self.radius)/self.v.x
        elif self.v.x < 0:
            return (self.p.x - self.radius)/abs(self.v.x)
        else:
            return Inf

    def horizontal_wall_collision_time(self):
        if self.v.y > 0:
            return (HEIGHT - self.p.y - self.radius)/self.v.y
        elif self.v.y < 0:
            return (self.p.y - self.radius)/abs(self.v.y)
        else:
            return Inf

    # Using Newtons second law (momentum form)
    def particle_collision(self, particle):
        dx, dy = particle.p.x - self.p.x, particle.p.y - self.p.y
        dvx, dvy = particle.v.x - self.v.x, particle.v.y - self.v.y
        dvdr = dx * dvx + dy * dvy
        dist = self.radius + particle.radius
        J = 2 * self.mass * particle.mass * dvdr / \
            ((self.mass + particle.mass) * dist)
        Jx = J * dx / dist
        Jy = J * dy / dist
        self.v.x += Jx / self.mass
        self.v.y += Jy / self.mass
        particle.v.x -= Jx / particle.mass
        particle.v.y -= Jy / particle.mass
        self.count += 1
        particle.count += 1

    # Collisions with walls causes the velocity's components to invert respectively
    def vertical_wall_collision(self):
        self.v.x = - self.v.x
        self.count += 1

    def horizontal_wall_collision(self):
        self.v.y = - self.v.y
        self.count += 1
