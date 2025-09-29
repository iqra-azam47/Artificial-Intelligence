import heapq

def a_star_search(graph, start, goal, heuristic):
    # Priority queue (cost + heuristic, current_node, path_taken)
    open_list = [(0 + heuristic[start], 0, start, [start])]
    visited = set()

    while open_list:
        est_total_cost, cost_so_far, node, path = heapq.heappop(open_list)

        # If we reached the goal, return path and cost
        if node == goal:
            return path, cost_so_far

        if node in visited:
            continue
        visited.add(node)

        # Explore neighbors
        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                g = cost_so_far + weight        # cost so far
                f = g + heuristic[neighbor]     # estimated total cost
                heapq.heappush(open_list, (f, g, neighbor, path + [neighbor]))

    return None, float("inf")  # No path found


# Example graph (like a map)
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 1), ('E', 5)],
    'C': [('F', 2)],
    'D': [('G', 3)],
    'E': [('G', 1)],
    'F': [('G', 2)],
    'G': []
}

# Example heuristic (straight-line guesses to goal 'G')
heuristic = {
    'A': 7,
    'B': 6,
    'C': 4,
    'D': 3,
    'E': 2,
    'F': 1,
    'G': 0
}

path, cost = a_star_search(graph, 'A', 'G', heuristic)
print("Shortest path:", path)
print("Total cost:", cost)