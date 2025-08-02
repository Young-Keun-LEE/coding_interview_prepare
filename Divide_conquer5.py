import sys
input = sys.stdin.readline

N, M = map(int, input().split(" "))
A_row = []
for _ in range(N):
    A_row.append(list(map(int, input().split(" "))))

M, K = map(int, input().split(" "))
B_col = [[] for _ in range(K)]
for _ in range(M):
    row = list(map(int, input().split(" ")))
    for j in range(K):
        B_col[j].append(row[j])

multiply = [[0] * K for _ in range(N)]
value = 0
for i in range(N):
    for j in range(K):
        for x in range(M):
            value += A_row[i][x] * B_col[j][x]
        multiply[i][j] += value
        value = 0

for i in range(N):
    print(" ".join(map(str,multiply[i])))