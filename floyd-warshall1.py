INF = float("inf")
V, E = map(int, input().split(" "))
distance = [[INF] * (V + 1) for _ in range(V + 1)]

for _ in range(E):
    a, b, c = map(int, input().split(" "))
    distance[a][b] = c

for k in range(1, V + 1): # floyd-warshall algorithm
    for i in range(1, V + 1):
        for j in range(1, V + 1):
            if distance[i][j] > distance[i][k] + distance[k][j]:
                distance[i][j] = distance[i][k] + distance[k][j]

route = INF
for i in range(1, V + 1): # Find shortest cycle
    route = min(route, distance[i][i])

if route == INF:
    print(-1)
else:
    print(route)