N = int(input()) # 1 < N <= 100
# dp[i][j] length = i, last_num = j

dp = [[0] * 10 for _ in range(N + 1)]

for j in range(1, 10):
    dp[1][j] = 1

for i in range(2, N + 1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i - 1][1]
        elif j == 9:
            dp[i][j] = dp[i - 1][8]
        else:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]

sum = 0
for j in range(10):
    sum += dp[N][j]

print(sum % int(1e9))