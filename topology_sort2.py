import heapq

n, m = map(int, input().split(" "))
indegree = [0] * (n + 1)
queue = []
graph = [[] for _ in range(n + 1)]
search = []

for _ in range(m):
    pre, post = map(int, input().split(" ")) # pre is followed by post
    graph[pre].append(post)
    indegree[post] += 1

for i in range(1, n + 1): 
    if indegree[i] == 0:
        heapq.heappush(queue, i)

while queue: # Make waiting queue with priority queue
    now = heapq.heappop(queue)
    search.append(now)
    for node in graph[now]:
        indegree[node] -= 1
        if indegree[node] == 0:
            heapq.heappush(queue, node)

print(*search)


