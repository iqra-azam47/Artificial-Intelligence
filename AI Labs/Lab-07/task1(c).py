## This code implements an Iterative Deepening Search (IDS) algorithm to
# traverse a graph by combining the benefits of DFS and BFS.

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

class IDS:
    def __init__(self, graph):
        self.graph = graph

    def search(self, start, goal):
        depth_limit = 0
        while True:
            print(f"\n--- Iterative Deepening Search (Depth Limit: {depth_limit}) ---")
            visited = set()
            path = []
            result = self._dls_recursive(start, goal, depth_limit, 0, visited, path)
            if result:
                return result
            
            if depth_limit > len(self.graph.adj_list) + 1: 
                print("\nGoal not found within a reasonable depth.")
                return None
            
            depth_limit += 1

    def _dls_recursive(self, current, goal, limit, depth, visited, path):
        if current == goal:
            print(f"Visiting node: {current} (Depth: {depth})")
            return path + [current]
        
        if depth >= limit:
            return None
        
        print(f"Visiting node: {current} (Depth: {depth})")
        visited.add(current)
        path.append(current)
        
        for neighbor in self.graph.adj_list.get(current, []):
            if neighbor not in visited:
                result = self._dls_recursive(neighbor, goal, limit, depth + 1, visited, path)
                if result:
                    return result
        
        path.pop()
        return None


graph_ids = Graph()
graph_ids.add_edge('A', 'B')
graph_ids.add_edge('A', 'F')
graph_ids.add_edge('A', 'D')
graph_ids.add_edge('A', 'E')
graph_ids.add_edge('B', 'K')
graph_ids.add_edge('B', 'J')
graph_ids.add_edge('K', 'N')
graph_ids.add_edge('K', 'M')
graph_ids.add_edge('D', 'G')
graph_ids.add_edge('D', 'C')
graph_ids.add_edge('E', 'C')
graph_ids.add_edge('E', 'H')
graph_ids.add_edge('E', 'I')
graph_ids.add_edge('I', 'L')

print("Adjacency List:")
graph_ids.print_graph()


ids_search = IDS(graph_ids)
path_to_G = ids_search.search('A', 'G')

if path_to_G:
    print(f"\nGoal node 'G' found! Path: {' -> '.join(path_to_G)}")