# Write a program to implement this graph in python.
#                     1
#                   / | \
#                 2   7  8
#                / \    / \
#               3   6  9  12
#              / \    / \
#             4   5  10 11



# Solution:

class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, u, v):
        if u not in self.adj_list:
            self.adj_list[u] = []
        self.adj_list[u].append(v)

    def print_graph(self):
        for node in self.adj_list:
            print(f"{node} --> {self.adj_list[node]}")

graph = Graph()

# Adding edges as per the tree
graph.add_edge(1, 2)
graph.add_edge(1, 7)
graph.add_edge(1, 8)
graph.add_edge(2, 3)
graph.add_edge(2, 6)
graph.add_edge(3, 4)
graph.add_edge(3, 5)
graph.add_edge(8, 9)
graph.add_edge(8, 12)
graph.add_edge(9, 10)
graph.add_edge(9, 11)

print("Adjacency List:")
graph.print_graph()
