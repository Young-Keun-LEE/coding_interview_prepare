from collections import deque
N = int(input())
numbers = list(map(int, input().split(" ")))

q = deque()

for i in range(len(numbers)):
    q.append((i + 1, numbers[i]))


for _ in range(N):
    index, num = q.popleft()
    if num > 0:
        q.rotate(1 - num)
    if num < 0:
        q.rotate(- num)
    print(index, end = " ")

