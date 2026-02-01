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
        self.all_paths = [[]]


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

    # def all_paths(self, start, end):
    #     def search(path, visited):
    #
    #         if start == end:
    #             self.all_paths.append(path)
    #         for u in graph.edges[start]:
    #             if u not in visited:
    #                 path.append(u)
    #                 visited.append(u)
    #                 search(path, visited)
    #                 path.pop()
    #                 visited.remove(u)


    def minimal_distance(self, start, end):
        pass


graph = Graph(["A", "B", "C", "D"])
graph.add_edge("A","C", 4)
graph.add_edge("A", "B", 2)
graph.add_edge("C","D", 14)
graph.add_edge("B","D", 1)
graph.add_edge("C","B", 8)
print(graph.edges)
print(graph.points)
print(graph.edges_count())
print(graph.points_count())



