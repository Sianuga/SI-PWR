import datetime

class Graph:
    def __init__(self):
        self.nodes = {}
        self.edges = []

    def add_node(self, name, lat, lon):
        node_id = f"{name} ({lat}, {lon})"
        if node_id not in self.nodes:
            self.nodes[node_id] = {"name": name, "lat": lat, "lon": lon}

    def add_edge(self, start, end, departure, arrival, line):
        delta = arrival - departure

        if delta.days < 0:
            delta = datetime.timedelta(days=1) + delta
        self.edges.append((start, end,departure, arrival, delta.total_seconds(), line))

    def get_edge_info(self, start, end):
        for edge in self.edges:
            if edge[0] == start and edge[1] == end:

                return edge[2]
        return None
    
    def get_neighbors(self, node):
        neighbors = []
        for edge in self.edges:
            if edge[0] == node:
                neighbors.append(edge[1])
        return neighbors
    
    def print_graph(self):
        for edge in self.edges:
            print (f"{edge[0]}, {edge[2].strftime('%H:%M:%S')} -> {edge[1]}, {edge[3].strftime('%H:%M:%S')} | Duration: {edge[4]} | Line: {edge[5]}")
    
    def get_neighbors_with_times(self, node, current_datetime):
        neighbors_with_times = []
        for edge in self.edges:
            start, end, departure, arrival, _, _ = edge
            if start == node and departure >= current_datetime:
                neighbors_with_times.append((end, departure, arrival))
        return neighbors_with_times
    
    def get_neighbors_with_times_and_lines(self, node, current_datetime):
        neighbors_with_times_and_lines = []
        for edge in self.edges:
            start, end, departure, arrival, _, line = edge
            if start == node and departure >= current_datetime:
                neighbors_with_times_and_lines.append((end, departure, arrival, line))
        return neighbors_with_times_and_lines