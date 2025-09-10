## This code implements a Depth-Limited Search (DLS) algorithm to
# traverse a graph up to a specified depth limit.

class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, u, v):
        if u not in self.adj_list:
            self.adj_list[u] = []
        self.adj_list[u].append(v)
        self.adj_list[u].sort(reverse=True)

    def print_graph(self):
        for node in self.adj_list:
            print(f"{node} --> {self.adj_list[node]}")

class DLS:
    def __init__(self, graph):
        self.graph = graph

    def search(self, start, goal, limit):
        return self._dls_recursive(start, goal, limit, 0, visited=set(), path=[])

    def _dls_recursive(self, current, goal, limit, depth, visited, path):
        print(f"Visiting node: {current} (Depth: {depth})")

        if current == goal:
            return path + [current]

        if depth >= limit:
            return None
        
        visited.add(current)
        path.append(current)

        for neighbor in self.graph.adj_list.get(current, []):
            if neighbor not in visited:
                result = self._dls_recursive(neighbor, goal, limit, depth + 1, visited, path)
                if result:
                    return result
        
        path.pop()
        return None


graph_dls = Graph()
graph_dls.add_edge('A', 'B')
graph_dls.add_edge('A', 'F')
graph_dls.add_edge('A', 'D')
graph_dls.add_edge('A', 'E')
graph_dls.add_edge('B', 'K')
graph_dls.add_edge('B', 'J')
graph_dls.add_edge('K', 'N')
graph_dls.add_edge('K', 'M')
graph_dls.add_edge('D', 'G')
graph_dls.add_edge('D', 'C')
graph_dls.add_edge('E', 'C')
graph_dls.add_edge('E', 'H')
graph_dls.add_edge('E', 'I')
graph_dls.add_edge('I', 'L')

print("Adjacency List:")
graph_dls.print_graph()



dls_search = DLS(graph_dls)
limit = 2
print(f"\n--- Depth-Limited Search (Limit = {limit}) ---")
path_to_G = dls_search.search('A', 'G', limit)

if path_to_G:
    print(f"\nGoal node 'G' found! Path: {' -> '.join(path_to_G)}")
else:
    print(f"\nGoal node 'G' not found within depth limit of {limit}.")