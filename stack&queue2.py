import sys
input = sys.stdin.readline
K = int(input())
stack = []
sum = 0
for _ in range(K):
    N = int(input())
    if N == 0:
        sum -= stack.pop()
    else:
        sum += N
        stack.append(N)

print(sum)