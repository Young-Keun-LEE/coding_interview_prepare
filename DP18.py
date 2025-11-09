N, M = map(int, input().split(" "))
memories = list(map(int, input().split(" ")))
costs = list(map(int, input().split(" ")))

# dp[cost] = the maximum memory we can free using exactly 'cost' units of cost
dp = [0] * (sum(costs) + 1)

# Iterate through each app
for i in range(N):
    # Update dp in reverse order to avoid reusing the same app multiple times (0/1 knapsack pattern)
    for j in range(len(dp) - 1, costs[i] - 1, -1):
        dp[j] = max(dp[j], dp[j - costs[i]] + memories[i])

# Find the minimum cost that frees at least M units of memory
for cost in range(len(dp)):
    if dp[cost] >= M:
        print(cost)
        exit(0)

# If it's impossible to free enough memory
print(-1)
