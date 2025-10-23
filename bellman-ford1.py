N, M = map(int, input().split(" "))
edges = []
INF = float("inf")
distance = [INF] * (N + 1)
distance[1] = 0

for _ in range(M):
    A, B, C = map(int, input().split(" ")) # Time is C from A to B
    edges.append((A, B, C))

for i in range(N - 1): # Find shortest distance
    updated = False
    for (a, b, c) in edges:
        if distance[b] > distance[a] + c:
            distance[b] = distance[a] + c
            updated = True
    if updated is False: # If distance is not updated, early stop loop
        break

if updated is True:
    for (a, b, c) in edges: # Find negative cycle
        if distance[b] > distance[a] + c:
            print(-1)
            exit()

for city in range(2, N + 1):
    if distance[city] == INF:
        print(-1)
    else:
        print(distance[city])
