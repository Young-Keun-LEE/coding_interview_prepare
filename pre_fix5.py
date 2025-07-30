import sys
input = sys.stdin.readline
board = []

N, M, K = map(int, input().strip().split())
prefix_sum = [[0] * (M + 1) for _ in range(N + 1)]

for _ in range(N):
    board.append(list(input().strip()))

for i in range(1, N + 1):
    for j in range(1, M + 1):
        if  (i + j) % 2 == 0:
            if board[i - 1][j - 1] == "B":
                prefix_sum[i][j] = prefix_sum[i - 1][j] + prefix_sum[i][j - 1] - prefix_sum[i - 1][j - 1]
            else:
                    prefix_sum[i][j] = prefix_sum[i - 1][j] + prefix_sum[i][j - 1] - prefix_sum[i - 1][j - 1] + 1
        else:
            if board[i - 1][j - 1] == "B":
                prefix_sum[i][j] = prefix_sum[i - 1][j] + prefix_sum[i][j - 1] - prefix_sum[i - 1][j - 1] + 1
            else:
                prefix_sum[i][j] = prefix_sum[i - 1][j] + prefix_sum[i][j - 1] - prefix_sum[i - 1][j - 1]

max_val, min_val = -float("inf"), float("inf")

for i in range(K, N + 1):
    for j in range(K, M + 1):
        wrong = prefix_sum[i][j] - prefix_sum[i - K][j] - prefix_sum[i][j - K] + prefix_sum[i - K][j - K]
        min_val = min(min_val, K * K - wrong, wrong)
print(min_val)
