import copy
n = int(input())
dp = []
array = []
for i in range(n):
    dp.append(list(map(int, input().split())))

array = copy.deepcopy(dp)

for i in range(1,n):
    for j in range(i + 1):
        if j == 0:
            dp[i][j] = dp[i - 1][j] + array[i][j]
            continue
            
        if j == i:
            dp[i][j] = dp[i - 1][j - 1] + array[i][j]
            continue
            
        dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + array[i][j]

max = -1
for j in range(n):
    if max < dp[n - 1][j]:
        max = dp[n - 1][j]
print(max)

