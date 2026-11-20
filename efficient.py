gap_cost = 30
pair_cost = [
    (0, 110, 48, 94),
    (110, 0, 118, 48),
    (48, 118, 0, 110),
    (94, 48, 110, 0)
]

def nw_score(X, Y, gap_cost):
    """Last row of the DP table, using O(len(Y)) space."""
    prev = [j * gap_cost for j in range(len(Y) + 1)]
    for i in range(1, len(X) + 1):
        curr = [i * gap_cost] + [0] * len(Y)
        for j in range(1, len(Y) + 1):
            curr[j] = min(
                prev[j - 1] + gap_cost(X[i - 1], Y[j - 1]),  # match/mismatch
                prev[j] + gap_cost,                            # gap in Y
                curr[j - 1] + gap_cost,                        # gap in X
            )
        prev = curr
    return prev


def hberg(X, Y, gap_cost):
    if len(X) == 0:
        return "_" * len(Y), Y
    if len(Y) == 0:
        return X, "_" * len(X)
    if len(X) == 1 or len(Y) == 1:
        return basic(X, Y)   # basic full-table version

    mid = len(X) // 2
    left = nw_score(X[:mid], Y, gap_cost)
    right = nw_score(X[mid:][::-1], Y[::-1], gap_cost)

    n = len(Y)
    k = min(range(n + 1), key=lambda j: left[j] + right[n - j])

    a1, b1 = hberg(X[:mid], Y[:k], gap_cost)
    a2, b2 = hberg(X[mid:], Y[k:], gap_cost)
    return a1 + a2, b1 + b2