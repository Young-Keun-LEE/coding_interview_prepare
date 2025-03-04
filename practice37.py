import sys
import heapq

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
        
input = sys.stdin.readline


while True:
    edges = []
    result = 0
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    for i in range(m):
        x, y, z = map(int, input().split())
        heapq.heappush(edges,(z, x, y))
    parent = [0] * (n + 1)
    
    for i in range(1, n + 1):
        parent[i] = i
        
    while edges:
        c, a, b = heapq.heappop(edges)
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
        else:
            result += c
    
    
    print(result)