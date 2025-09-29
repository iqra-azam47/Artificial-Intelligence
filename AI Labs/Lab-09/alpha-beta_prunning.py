import math

# Alpha-Beta Pruning
def alphabeta(node, depth, alpha, beta, maximizingPlayer, values, index=0):
    if depth == 0 or index >= len(values):
        return values[index]

    if maximizingPlayer:
        value = -math.inf
        value = max(value, alphabeta(node*2, depth-1, alpha, beta, False, values, index*2))
        alpha = max(alpha, value)
        if alpha < beta:
            value = max(value, alphabeta(node*2+1, depth-1, alpha, beta, False, values, index*2+1))
            alpha = max(alpha, value)
        return value
    else:
        value = math.inf
        value = min(value, alphabeta(node*2, depth-1, alpha, beta, True, values, index*2))
        beta = min(beta, value)
        if alpha < beta:
            value = min(value, alphabeta(node*2+1, depth-1, alpha, beta, True, values, index*2+1))
            beta = min(beta, value)
        return value


# ------------ TEST -------------
values = [3, 5, 2, 9, 12, 5, 23, 23]
depth = 3
print("The optimal value with Alpha-Beta Pruning is:", alphabeta(0, depth, -math.inf, math.inf, True, values))