import math

# Minimax function
def minimax(node, depth, maximizingPlayer, values, index=0):
    # Base case: leaf node or depth 0
    if depth == 0 or index >= len(values):
        return values[index]

    if maximizingPlayer:
        best = -math.inf
        # left child
        val = minimax(node*2, depth-1, False, values, index*2)
        best = max(best, val)
        # right child
        val = minimax(node*2+1, depth-1, False, values, index*2+1)
        best = max(best, val)
        return best
    else:
        best = math.inf
        # left child
        val = minimax(node*2, depth-1, True, values, index*2)
        best = min(best, val)
        # right child
        val = minimax(node*2+1, depth-1, True, values, index*2+1)
        best = min(best, val)
        return best


# ------------ TEST -------------
# Leaf node values (example game tree leaves)
values = [3, 5, 2, 9, 12, 5, 23, 23]
depth = 3   # tree depth
print("The optimal value is:", minimax(0, depth, True, values))