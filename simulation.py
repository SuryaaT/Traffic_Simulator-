class Simulation:
    def __init__(self):
        self.roads = []
        self.junctions = []
        self.sources = []
        self.sinks = []
        self.time = 0
        self.sink_map = {}

    def build_sink_map(self):
        self.sink_map = {s.junction: s for s in self.sinks}

    def step(self):

        if not self.sink_map:
            self.build_sink_map()

        # 1. generate vehicles
        for s in self.sources:
            s.step(self.time)

        # 2. smooth movement
        for road in self.roads:
            for v in road.vehicles:
                v.progress += 0.02  # <-- smooth motion

        # 3. junction control
        for j in self.junctions:
            j.step()

        # 4. collect vehicles at sinks
        for road in self.roads:
            remaining = []

            for v in road.vehicles:
                if v.progress >= 1 and v.current_road_index == len(v.path) - 1:
                    sink = self.sink_map.get(road.end)
                    if sink:
                        sink.collect(v, self.time)
                else:
                    remaining.append(v)

            road.vehicles = type(road.vehicles)(remaining)

        self.time += 1