class Event:
    def __init__(self, time, a, b):
        self.time = time
        self.particle_a = a
        self.particle_b = b
        if a != None:
            self.countA = self.particle_a.count
        if b != None:
            self.countB = self.particle_b.count

    # Used for the priority queue's/list's sorting function
    def __lt__(self, event):
        return self.time < event.time

    def is_invalid(self):
        return (self.particle_a != None and self.countA != self.particle_a.count) or (self.particle_b != None and self.countB != self.particle_b.count)
