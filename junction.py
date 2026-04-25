class Junction:
    def __init__(self, jid):
        self.id = jid
        self.incoming = []
        self.outgoing = []
        self.last_served = 0

    def add_incoming(self, r):
        self.incoming.append(r)

    def add_outgoing(self, r):
        self.outgoing.append(r)

    def step(self):
        if not self.incoming:
            return

        n = len(self.incoming)

        for i in range(n):
            idx = (self.last_served + i) % n
            road = self.incoming[idx]

            if road.vehicles:
                v = road.vehicles[0]

                if v.progress >= 1:
                    if v.current_road_index == len(v.path) - 1:
                        road.vehicles.popleft()
                        self.last_served = idx + 1
                        return

                    next_road = v.path[v.current_road_index + 1]

                    if next_road.can_enter():
                        road.vehicles.popleft()
                        v.current_road_index += 1
                        v.progress = 0
                        next_road.add_vehicle(v)

                        self.last_served = idx + 1
                        return