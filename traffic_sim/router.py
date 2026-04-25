from collections import deque

class Router:
    def __init__(self, graph):
        self.graph = graph

    def get_path(self, source, dest):
        q = deque([(source, [])])
        visited = set([source])

        while q:
            node, path = q.popleft()

            if node == dest:
                return path

            for road in self.graph.get(node, []):
                nxt = road.end
                if nxt not in visited:
                    visited.add(nxt)
                    q.append((nxt, path + [road]))

        return None