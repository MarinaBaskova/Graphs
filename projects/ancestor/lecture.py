class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        if vertex not in self.vertices:
            self.vertices[vertex] = set()
        else:
            print("WARNING: vertex does exist")

    def add_edge(self, vertex_from, vertex_to):
        """
        Add a directed edge to the graph.
        """
        if vertex_from in self.vertices or vertex_to in self.vertices:
            self.vertices[child].add(parent)

        else:
            print("WARNING: vertex does not exist")


def earliest_ancestor(ancestors, starting_node):
