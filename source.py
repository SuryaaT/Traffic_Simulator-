import random
from traffic_sim.vehicle import Vehicle

class Source:
    def __init__(self, junction, rate, destinations, router):
        self.junction = junction
        self.rate = rate
        self.destinations = destinations
        self.router = router
        self.counter = 0

        self.colors = ["r", "g", "b", "m", "c", "y"]

        # destination-based color mapping
        self.dest_color_map = {
            dest: self.colors[i % len(self.colors)]
            for i, dest in enumerate(self.destinations)
        }

    def step(self, time):
        if random.random() < self.rate:
            dest = random.choice(self.destinations)

            path = self.router.get_path(self.junction, dest)
            if not path:
                return

            color = self.dest_color_map[dest]

            v = Vehicle(self.counter, self.junction, dest, path, color)
            v.start_time = time
            self.counter += 1

            first = path[0]
            if first.can_enter():
                first.add_vehicle(v)