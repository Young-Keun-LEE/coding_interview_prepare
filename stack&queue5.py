from collections import deque
N, K = map(int, input().split(" "))
q = deque()
removed = []

for i in range(1, N + 1):
    q.append(i)

while len(q) > 0:
    q.rotate(1 - K)
    removed.append(q.popleft())

print(f"<{', '.join(map(str, removed))}>")
