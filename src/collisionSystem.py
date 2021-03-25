from setup import pygame, Inf, WIN, BACKGROUND_COLOR, heappush, heappop, sleep
from event import Event


class CollisionSystem:
    def __init__(self, particles):
        self.pq = []
        self.time = 0.0
        self.particles = particles

    def predict_collision(self, obj):
        if obj == None:
            return
        for particle in self.particles:
            dt = obj.particle_collision_time(particle)
            if dt < Inf:
                heappush(self.pq, Event(self.time + dt, obj, particle))
        if obj.vertical_wall_collision_time() < Inf:
            heappush(self.pq, Event(
                self.time + obj.vertical_wall_collision_time(), obj, None))
        if obj.horizontal_wall_collision_time() < Inf:
            heappush(self.pq, Event(
                self.time + obj.horizontal_wall_collision_time(), None, obj))

    def redraw_window(self):
        heappush(self.pq, Event(self.time + 1.0, None, None))

    def simulate(self):
        # Appending the redraw_window event before the main-loop of the simulation
        heappush(self.pq, Event(0.0, None, None))
        for particle in self.particles:
            self.predict_collision(particle)

        # The main-loop of the simulation
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
            WIN.fill(BACKGROUND_COLOR)
            event = heappop(self.pq)
            if event.is_invalid():
                continue
            # Sleep is added for reducing CPU usage
            sleep(0.002)
            a = event.particle_a
            b = event.particle_b
            for particle in self.particles:
                particle.move(event.time - self.time)
                particle.draw()
            self.time = event.time
            pygame.display.update()

            # Checking for collisions, if no collisions redraw the window
            if a != None and b != None:
                a.particle_collision(b)
                self.predict_collision(a)
                self.predict_collision(b)
            elif a != None and b == None:
                a.vertical_wall_collision()
                self.predict_collision(a)
            elif a == None and b != None:
                b.horizontal_wall_collision()
                self.predict_collision(b)
            else:
                self.redraw_window()
