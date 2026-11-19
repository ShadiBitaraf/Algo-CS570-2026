gap_cost = 30
pair_cost = [
    (0, 110, 48, 94),
    (110, 0, 118, 48),
    (48, 118, 0, 110),
    (94, 48, 110, 0)
]
idx = {'A': 0, 'C': 1, 'G': 2, 'T': 3}

def basic(s1:str, s2:str):

    rows = len(s1) + 1
    cols = len(s2) + 1
    opt = [[0 for _ in range(cols)] for _ in range(rows)]

    for i in range(rows):
        opt[i][0] = i * gap_cost
    for j in range(cols):
        opt[0][j] = j * gap_cost

    for i in range(1, rows):
        for j in range(1, cols):
            
            opt[i][j] = min (
                opt[i - 1][j - 1] + pair_cost[idx[s1[i - 1]]][idx[s2[j - 1]]],
                opt[i - 1][j] + gap_cost,
                opt[i][j - 1] + gap_cost
            )

    return opt[rows - 1][cols - 1]