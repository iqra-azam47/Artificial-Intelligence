from queue import PriorityQueue

# Graph ko dictionary ke form mein define karte hain
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Heuristic values (manually assigned for example)
# Yeh usually goal tak ke estimated distance hotay hain
heuristic = {
    'A': 5,
    'B': 4,
    'C': 3,
    'D': 7,
    'E': 2,
    'F': 0   # goal node
}

def greedy_bfs(start, goal):
    visited = []
    pq = PriorityQueue()
    pq.put((heuristic[start], start))

    while not pq.empty():
        h, current = pq.get()
        visited.append(current)

        print(f"Visited: {current}")

        if current == goal:
            print("Goal found!")
            return visited

        for neighbor in graph[current]:
            if neighbor not in visited:
                pq.put((heuristic[neighbor], neighbor))

    return visited

# Example run
path = greedy_bfs('A', 'F')
print("Path explored:", path)


# Output:
# Visited: A
# Visited: C
# Visited: F
# Goal found!