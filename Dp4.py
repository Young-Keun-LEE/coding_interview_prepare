import sys
input = sys.stdin.readline

N = int(input())
dp = [0] * (N + 1)
wines = [0]

for i in range(N):
    wines.append(int(input()))

dp[1] = wines[1]
if N >= 2:
    dp[2] = wines[1] + wines[2]

if N >= 3:
    dp[3] = max(wines[1] + wines[2], wines[2] + wines[3], wines[1] + wines[3])

for i in range(4, N + 1):
    dp[i] = max(dp[i - 1], dp[i - 2] + wines[i], dp[i - 3] + wines[i - 1] + wines[i])

print(dp[N])
