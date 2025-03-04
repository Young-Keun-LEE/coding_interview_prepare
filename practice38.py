import sys
import heapq

input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n = int(input())
x = []
y = []
z = []

parent = [0] * (n + 1)

for i in range(1, n + 1):
    parent[i] = i

for i in range(1, n + 1):
    a, b, c = map(int, input().split())
    x.append((a, i))
    y.append((b, i))
    z.append((c, i))

x.sort()
y.sort()
z.sort()

q = []

for i in range(n - 1):
    heapq.heappush(q, (x[i + 1][0] - x[i][0], x[i][1], x[i + 1][1]))
    heapq.heappush(q, (y[i + 1][0] - y[i][0], y[i][1], y[i + 1][1]))
    heapq.heappush(q, (z[i + 1][0] - z[i][0], z[i][1], z[i + 1][1]))

result = 0

while q:
    cost, a, b = heapq.heappop(q)
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)