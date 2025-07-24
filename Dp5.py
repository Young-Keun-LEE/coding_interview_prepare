N = int(input())
A = list(map(int, input().split(" ")))

dp = [1] * N

for i in range(N):
    for j in range(i):
        if A[j] < A[i]:
            dp[i] = max(dp[i], dp[j] + 1)

max_val = -1
for i in range(N):
    max_val = max(max_val, dp[i])

print(max_val)