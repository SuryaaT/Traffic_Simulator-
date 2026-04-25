from collections import deque

class Road:
    def __init__(self, rid, start, end, capacity=5, length=30):
        self.id = rid
        self.start = start
        self.end = end
        self.capacity = capacity
        self.length = length

        self.vehicles = deque()

    def can_enter(self):
        # capacity check
        if len(self.vehicles) >= self.capacity:
            return False

        # spacing check (IMPORTANT)
        if self.vehicles:
            last_vehicle = self.vehicles[-1]
            if last_vehicle.progress < 0.2:
                return False

        return True

    def add_vehicle(self, v):
        v.progress = 0
        self.vehicles.append(v)