INF = int(1e9)
N, M = map(int, input().split()) #Enter the number of company and path
graph = [[INF] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    graph[i][i] = 0
    
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
    
X, K = map(int, input().split()) # X is destination and K is stopover

for k in range(1, N + 1): # Do floyd-warshall algorithm
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
            
# Calculate minimum time of moving, total minimum time is add min(1 -> k) and min(k -> x)
if graph[1][K] + graph[K][X] >= INF:
    print(-1)
else:
    print(graph[1][K] + graph[K][X])