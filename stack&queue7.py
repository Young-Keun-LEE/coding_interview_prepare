from collections import deque
N = int(input())
A = list(map(int,input().split(" ")))
B = list(map(int,input().split(" ")))
M = int(input())
C = list(map(int,input().split(" ")))

q = deque()

for i in range(len(A)):
    if A[i] == 0:
        q.append(B[i])

result = []

for element in C:
    q.appendleft(element)
    result.append(q.pop())

print(" ".join(map(str,result)))