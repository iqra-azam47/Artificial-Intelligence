## You are given the following tree whose starting node is A and Goal node is G

#                       A
#                   / / |  \   
#                 B   F D    E
#                / \    |   / | \
#               K   J   G  C  H  I
#              / \               |
#             N   M              L


class Graph:
    def __init__(self):
        self.adj_list = {}



    def add_edge(self, u, v):
        if u not in self.adj_list:
            self.adj_list[u] = []
        self.adj_list[u].append(v)
        # Sort neighbors in reverse alphabetical order for consistent LIFO processing
        self.adj_list[u].sort(reverse=True)



    def print_graph(self):
        for node in self.adj_list:
            print(f"{node} --> {self.adj_list[node]}")


    # Iterative DFS to find path from start to goal
    def dfs_iterative(self, start, goal):
       
        stack = [start]
        visited = set()
        path = []

        while stack:
            current_node = stack.pop()

            if current_node not in visited:
                print(f"Visiting node: {current_node}")
                path.append(current_node)
                visited.add(current_node)

                if current_node == goal:
                    print(f"\nGoal node '{goal}' found!")
                    return path

                neighbors = self.adj_list.get(current_node, [])
                for neighbor in neighbors:
                    if neighbor not in visited:
                        stack.append(neighbor)
        
        print(f"\nGoal node '{goal}' not found.")
        return None

# Creating the graph based on the tree image
graph = Graph()
graph.add_edge('A', 'B')
graph.add_edge('A', 'F')
graph.add_edge('A', 'D')
graph.add_edge('A', 'E')
graph.add_edge('B', 'K')
graph.add_edge('B', 'J')
graph.add_edge('K', 'N')
graph.add_edge('K', 'M')
graph.add_edge('D', 'G')
graph.add_edge('D', 'C')
graph.add_edge('E', 'C')
graph.add_edge('E', 'H')
graph.add_edge('E', 'I')
graph.add_edge('I', 'L')

print("Adjacency List:")
graph.print_graph()

print("\n--- Starting DFS Traversal ---")
path_to_G = graph.dfs_iterative(start='A', goal='G')
if path_to_G:
    print(f"Path to goal 'G': {' -> '.join(path_to_G)}")
