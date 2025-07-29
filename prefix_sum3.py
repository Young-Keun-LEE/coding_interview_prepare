import sys
input = sys.stdin.readline
A = []
N, M = map(int, input().split(" "))

for _ in range(N):
    A.append(list(map(int, input().strip().split(" "))))

prefix_sum = [[0] * (N + 1) for _ in range(N + 1)]

result = []
for i in range(1, N + 1):
    for j in range(1, N + 1):
        prefix_sum[i][j] = prefix_sum[i - 1][j] + prefix_sum[i][j - 1] + A[i - 1][j - 1] - prefix_sum[i - 1][j - 1]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().strip().split(" "))      
    result.append(prefix_sum[x2][y2] - prefix_sum[x1 - 1][y2] - prefix_sum[x2][y1 - 1] + prefix_sum[x1 - 1][y1 - 1])    

print("\n".join(map(str, result)))
