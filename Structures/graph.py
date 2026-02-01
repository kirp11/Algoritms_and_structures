class Edge:
    def __init__(self, start, end, weight):
        self.start = start
        self.end = end
        self.weight = weight

    def __repr__(self):
        return f"Edge({self.start}, {self.end}, {self.weight})"


class Graph:

    def __init__(self, points):
        self.points = points
        self.edges = {}


    def add_edge(self,start, end, weight = 0):
        edge = Edge(start, end, weight)
        reversed_edge = Edge(end, start, weight)

        if start not in self.edges:
            self.edges[start] = []
        if end not in self.edges:
            self.edges[end] = []
        self.edges[start].append(edge)
        self.edges[end].append(reversed_edge)


    def edges_count(self):
        return len(self.edges)

    def points_count(self):
        return len(self.points)

    def paths(self, start, end_point):
        all_paths = {}

        def find_path(current_node, path, weight):
            path = path + current_node
            if current_node == end_point:
                all_paths[path] = weight
                return
            for edge in self.edges[current_node]:
                next_node = edge.end
                weight += edge.weight
                if next_node not in path:
                    find_path(next_node, path, weight)

        find_path(start, "", 0)

        return all_paths



    def minimal_distance(self, start, end):
        paths = self.paths(start, end)
        min_val = min(paths.values())
        keys = [k for k, v in paths.items() if v == min_val]
        for key in keys:
            print(f"минимальная дистанция составляет {paths[key]} км по маршруту {key}")



graph = Graph(["A", "B", "C", "D"])
graph.add_edge("A","C", 4)
graph.add_edge("A", "B", 2)
graph.add_edge("C","D", 14)
graph.add_edge("B","D", 1)
graph.add_edge("C","B", 8)
# print(graph.edges["A"])
# print(graph.points)
# print(graph.edges_count())
# print(graph.points_count())
graph.minimal_distance("A", "D")



