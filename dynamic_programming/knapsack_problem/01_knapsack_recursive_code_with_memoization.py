w = [60, 100, 120]
val = [10, 20, 30]
W = 180
N = len(val)

t = [[-1 for i in range(W+1)] for i in range(N+1)]

#### DP = Recursion + Storage

def knapsack(w, val, W, N):
    # Base Case
    if W == 0 or N == 0:
        return 0

    # Memoization
    if t[N][W] != -1:
        return t[N][W]

    # Choice Diagram
    if w[N-1] > W:
        t[N][W] = knapsack(w, val, W, N-1)
        return t[N][W]
    else:
        t[N][W] = max(
            val[N-1] + knapsack(w, val, W-w[N-1], N-1), knapsack(w, val, W, N-1)
        )
        return t[N][W]

print(knapsack(w, val, W, N))