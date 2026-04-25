class Vehicle:
    def __init__(self, vid, source, destination, path, color="r"):
        self.id = vid
        self.source = source
        self.destination = destination
        self.path = path

        self.current_road_index = 0
        self.progress = 0

        self.start_time = None
        self.end_time = None

        self.color = color