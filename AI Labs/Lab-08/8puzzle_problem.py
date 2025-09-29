import heapq

# Calculate Manhattan distance as heuristic
def manhattan_distance(state, goal):
    distance = 0
    for num in range(1, 9):
        x1, y1 = [(i, row.index(num)) for i, row in enumerate(state) if num in row][0]
        x2, y2 = [(i, row.index(num)) for i, row in enumerate(goal) if num in row][0]
        distance += abs(x1 - x2) + abs(y1 - y2)
    return distance

# Generate neighbor states by moving the blank (0)
def get_neighbors(state):
    neighbors = []
    state_list = [list(row) for row in state]
    # find blank (0) position
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                x, y = i, j
    # possible moves: up, down, left, right
    moves = [(-1,0),(1,0),(0,-1),(0,1)]
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state_list]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(tuple(tuple(row) for row in new_state))
    return neighbors

# A* search algorithm
def a_star_8puzzle(start, goal):
    open_list = []
    heapq.heappush(open_list, (manhattan_distance(start, goal), 0, start, [start]))
    visited = set()
    
    while open_list:
        f, g, current, path = heapq.heappop(open_list)
        if current == goal:
            return path  # return the solution path
        
        if current in visited:
            continue
        visited.add(current)
        
        for neighbor in get_neighbors(current):
            if neighbor not in visited:
                h = manhattan_distance(neighbor, goal)
                heapq.heappush(open_list, (g + 1 + h, g + 1, neighbor, path + [neighbor]))
    
    return None  # no solution

# Example usage:
start = (
    (1, 2, 3),
    (4, 0, 6),
    (7, 5, 8)
)

goal = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 0)
)

solution = a_star_8puzzle(start, goal)

if solution:
    print("Solution found in", len(solution)-1, "moves:")
    for step in solution:
        for row in step:
            print(row)
        print()
else:
    print("No solution found")
