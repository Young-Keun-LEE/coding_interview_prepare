import heapq

def dijkstra(graph, node1, node2): # Calculate shortest distance from node1 to node2
    distance = [INF] * (N + 1)
    queue = [(0, node1)]
    distance[node1] = 0

    while queue:
        dist, now = heapq.heappop(queue)
        if dist > distance[now]:
            continue
        for neighbor in graph[now]:
            next, weight = neighbor
            if distance[next] > distance[now] + weight:
                distance[next] = distance[now] + weight
                heapq.heappush(queue, (distance[next], next))
    
    return distance[node2]

INF = float("inf")
N, E = map(int, input().split(" "))
graph = [[] for _ in range(N + 1)]

for _ in range(E):
    a, b, c = map(int, input().split(" "))
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split(" ")) # Must visit v1, v2

path1 = dijkstra(graph, 1, v1) + dijkstra(graph, v1, v2) + dijkstra(graph, v2, N)# 1 -> v1 -> v2 -> N
path2 = dijkstra(graph, 1, v2) + dijkstra(graph, v2, v1) + dijkstra(graph, v1, N)# 1 -> v2 -> v1 -> N

shortest_path = min(path1, path2)
print(-1 if shortest_path == INF else shortest_path)