from collections import deque
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

distance = [-1] * (n + 1)
distance[x] = 0

q = deque([x])
while q:
    city = q.popleft()
    for c in graph[city]:
        if distance[c] == -1:
            distance[c] = distance[city] + 1
            q.append(c)

exist = False
for i in range(1, n + 1):
    if distance[i] == k:
        exist = True
        print(i)

if exist is False:
    print(-1)