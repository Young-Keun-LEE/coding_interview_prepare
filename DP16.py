W = int(input())  # Number of weights
weights = list(map(int, input().split()))
M = int(input())  # Number of marbles
marbles = list(map(int, input().split()))

# dp[i][j] = True if it's possible to measure weight j using the first i weights
dp = [[False] * (sum(weights) + 1) for _ in range(W + 1)]
dp[0][0] = True  # Base case: zero weight with zero weights

for i in range(1, W + 1):
    weight = weights[i - 1]
    for j in range(sum(weights) + 1):
        if dp[i-1][j]:
            # Three options for the current weight:
            # 1. Do not use it
            # 2. Place it on the same side as the marble
            # 3. Place it on the opposite side
            if j + weight <= sum(weights):
                dp[i][j + weight] = True
            dp[i][j] = dp[i][abs(j - weight)] = True

for marble in marbles:
    if marble > sum(weights):
        print("N", end = " ")
    else:
        print("Y" if dp[W][marble] else "N", end=" ")
