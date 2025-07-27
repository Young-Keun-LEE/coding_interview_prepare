import sys
input = sys.stdin.readline

N, K = map(int, input().split(" ")) # N is the number of item and K is max weight to carry
weight = [0]
value = [0]
dp = [[0] * (K + 1) for _ in range(N + 1)]

for _ in range(N):
    W, V = map(int, input().split(" "))
    weight.append(W)
    value.append(V)

for i in range(1, N + 1):
    for w in range(K + 1):
        if weight[i] > w:
            dp[i][w] = dp[i - 1][w]
        else:
            dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weight[i]] + value[i])

print(dp[N][K])