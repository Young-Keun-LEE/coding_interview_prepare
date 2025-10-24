import heapq
INF = float("inf")
T = int(input())


def dijkstra(start, graph):
    distance = [INF] * len(graph)
    distance[start] = 0
    pq = [(0, start)]

    while pq:
        dist, now = heapq.heappop(pq)
        if distance[now] < dist:
            continue
        for next, cost in graph[now]:
            new_cost = dist + cost
            if new_cost < distance[next]:
                distance[next] = new_cost
                heapq.heappush(pq, (new_cost, next))
    return distance


for _ in range(T):
    n, m, t = map(int, input().split(" "))
    s, g, h = map(int, input().split(" "))
    graph = [[] for _ in range(n + 1)]
    distinations = []
    distance = [INF] * (n + 1)

    for _ in range(m):
        a, b, d = map(int, input().split(" "))
        graph[a].append((b, d))
        graph[b].append((a, d))
    for _ in range(t):
        x = int(input())
        distinations.append(x)
    distinations.sort()
    # Test start -> dist == (start -> g -> h -> dist) or (start -> h -> g -> dist)
    start_from_s = dijkstra(s, graph)
    start_from_h = dijkstra(h, graph)
    start_from_g = dijkstra(g, graph)
    for node, cost in graph[g]:
        if node == h:
            gh = cost
    for dist in distinations:
        sd = start_from_s[dist]
        sg = start_from_s[g]
        sh = start_from_s[h]
        hd = start_from_h[dist]
        gd = start_from_g[dist]


        # -------test --------
        if sd != INF and sd == min(sg + gh + hd, sh + gh +gd):
            print(dist, end = " ")