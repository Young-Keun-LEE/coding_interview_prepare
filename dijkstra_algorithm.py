import sys
input = sys.stdin.readline
INF = int(1e9)

N, M = map(int, input().split()) # The number of node and edge

start = int(input()) # Enter starting node
graph = [[] for i in range(N + 1)]
visited = [False] * (N + 1)
distance = [INF] * (N + 1)

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

def get_smallest_node():
    min = INF
    for i in range(1, N + 1):
        if visited[i] == False:
            if min > distance[i]:
                min = distance[i]
                min_index = i
    if min == INF:
        return None
    
    return min_index

def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    while True:
        shortest_node = get_smallest_node()
        if shortest_node == None:
            break
        for i in graph[shortest_node]:
            if distance[i[0]] > i[1]:
                distance[i[0]] = i[1]

dijkstra(start)

for i in range(1, N + 1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])