import sys
input = sys.stdin.readline
print = sys.stdout.write

dp = [0] * 101
dp[1], dp[2], dp[3] = 1, 1, 1

T = int(input().strip())
result = []

for i in range(4, 101):
    dp[i] = dp[i - 2] + dp[i - 3]

for _ in range(T):
    N = int(input().strip())
    result.append(dp[N])
    
print("\n".join(map(str,result)) + "\n")
