from collections import deque
n = int(input()) # The number of node
e = int(input()) # The number of edge
edges = [[] for _ in range(n + 1)]
cnt = 0
visited = [0] * (n + 1)

for _ in range(e):
    u, v = map(int, input().split(" "))
    edges[v].append(u)
    edges[u].append(v)

queue = deque()
queue.append(1)
visited[1] = 1

while queue:
    now = queue.popleft()
    for nxt in edges[now]:
        if visited[nxt] == 0:
            visited[nxt] = 1
            queue.append(nxt)
            cnt += 1

print(cnt)