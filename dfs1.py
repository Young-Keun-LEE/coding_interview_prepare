N, M, R = map(int, input().split(" "))
cnt = 1
edges = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
stack = [R]

for _ in range(M):
    u, v = map(int, input().split(" ")) # u < v
    edges[u].append(v)
    edges[v].append(u)

for i in range(len(edges)):
    edges[i].sort(reverse=True)

while stack:
    node = stack.pop()  
    if visited[node] == 0:
        visited[node] = cnt
        cnt += 1
        for nxt in edges[node]:
            if visited[nxt] == 0:
                stack.append(nxt)
    
for i in range(1, N + 1):
    print(visited[i])

