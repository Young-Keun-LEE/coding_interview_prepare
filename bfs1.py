from collections import deque

N, M, R = map(int, input().split(" "))
edges = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
cnt = 1

for _ in range(M):
    u, v = map(int, input().split(" ")) # (u, v)
    edges[u].append(v)
    edges[v].append(u)

for i in range(len(edges)):
    edges[i].sort()
    
queue = deque()
visited[R] = cnt
cnt += 1
queue.append(R)

while queue:
    node = queue.popleft()
    for nxt in edges[node]:
        if visited[nxt] == 0:
            visited[nxt] = cnt
            cnt += 1
            queue.append(nxt)

for i in range(1, N + 1):
    print(visited[i])

