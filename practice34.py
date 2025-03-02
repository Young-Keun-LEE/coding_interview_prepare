import sys
import heapq

INF = int(1e9)
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)
for i in range(m):
  a, b = map(int, input().split())  # a and b is connected
  graph[a].append((b, 1))
  graph[b].append((a, 1))

start = 1
q = []
distance[start] = 0
heapq.heappush(q, (0, start))
while q:
  dist, node = heapq.heappop(q)
  if distance[node] < dist:
    continue

  for data in graph[node]:
    cost = dist + 1
    if cost < distance[data[0]]:
      distance[data[0]] = cost
      heapq.heappush(q, (cost, data[0]))

max = -1
node = n + 2
count = -1
for i in range(1, n + 1):
  if distance[i] == max:
    count += 1
    if node > i:
      node = i
  elif distance[i] > max:
    max = distance[i]
    count = 1
    node = i

print(node, max, count, end=" ")
