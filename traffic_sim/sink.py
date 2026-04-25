class Sink:
    def __init__(self, junction):
        self.junction = junction
        self.completed = []

    def collect(self, v, time):
        v.end_time = time
        self.completed.append(v)

    def avg_time(self):
        if not self.completed:
            return 0
        return sum(v.end_time - v.start_time for v in self.completed) / len(self.completed)