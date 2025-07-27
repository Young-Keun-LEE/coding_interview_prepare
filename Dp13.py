N = int(input())
A = list(map(int, input().split(" ")))

lis = [1] * N
lds = [1] * N

for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            lis[i] = max(lis[j] + 1, lis[i])
        
for i in range(N - 1, -1, -1):
    for j in range(N - 1, i, -1):
        if A[i] > A[j]:
            lds[i] = max(lds[i], lds[j] + 1)

max_len = -1

for i in range(N):
    length = lis[i] + lds[i] - 1
    if max_len < length:
        max_len = length

print(max_len)