import copy
t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    array = list(map(int, input().split()))
    dp = []
    for i in range(0, n * m, m):
        dp.append(array[i:i + m])
    array = copy.deepcopy(dp)
    result = 0

    for i in range(1, m): # Calculate dp[j][i], Move is only three cases
        for j in range(n):
            if j == 0:  
                dp[j][i] = max(dp[j][i], dp[j][i - 1] + array[j][i], dp[j + 1][i - 1] + array[j][i])
            elif j == n - 1:
                dp[j][i] = max(dp[j][i], dp[j][i - 1] + array[j][i], dp[j - 1][i - 1] + array[j][i])
            else:
                dp[j][i] = max(dp[j][i], dp[j][i - 1] + array[j][i], dp[j - 1][i - 1] + array[j][i], dp[j + 1][i - 1] + array[j][i] )

    for i in range(n):
        if result < dp[i][m - 1]:
            result = dp[i][m - 1]
    print(result)