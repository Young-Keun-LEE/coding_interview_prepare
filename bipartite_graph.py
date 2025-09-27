from collections import deque
k = int(input())

def bipartite_graph(graph, max_node):
    queue = deque()
    for node in range(1, max_node + 1):
        if colored[node] != 0:
            continue

        queue.append(node)
        colored[node] = 1
        while queue:
            now = queue.popleft()
            for neighbor in graph[now]:
                if colored[neighbor] == 0:
                    colored[neighbor] = -colored[now]
                    queue.append(neighbor)
                elif colored[neighbor] == colored[now]:
                    return False
    return True

for _ in range(k):
    v, e = map(int, input().split(" "))
    colored = [0] * (v + 1)
    graph = [[] for _ in range(v + 1)]
    for _ in range(e):
        u, x = map(int, input().split(" "))
        graph[u].append(x)
        graph[x].append(u)
    print("YES" if bipartite_graph(graph, v) else "NO")



