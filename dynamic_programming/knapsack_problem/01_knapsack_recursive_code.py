w = [60, 100, 120]
val = [10, 20, 30]
W = 120
N = len(val)

def knapsack(w, val, W, N):
    # Base Case
    if W == 0 or N == 0:
        return 0

    # Choice Diagram
    if w[N-1] > W:
        return knapsack(w, val, W, N-1)
    else:
        return max(
            val[N-1] + knapsack(w, val, W-w[N-1], N-1), knapsack(w, val, W, N-1)
        )

print(knapsack(w, val, W, N))