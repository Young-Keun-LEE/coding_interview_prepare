import heapq

INF = float("inf")
V, E= map(int, input().split(" "))
k = int(input()) # start node
graph = [[] for _ in range(V + 1)]
distance = [INF] * (V + 1)
queue = []

for _ in range(E):
    u, v, w = map(int, input().split(" "))
    graph[u].append((v, w))

distance[k] = 0 # Set start node distance to 0
heapq.heappush(queue, (0, k)) # (distance, node)
while queue:
    now_dist, now_node = heapq.heappop(queue)
    if now_dist > distance[now_node]: 
        continue
    for neighbor in graph[now_node]:
        new_distance = now_dist + neighbor[1]
        if distance[neighbor[0]] > new_distance:
            distance[neighbor[0]] = new_distance
            heapq.heappush(queue, (new_distance, neighbor[0]))
    
for i in range(1, V + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])

