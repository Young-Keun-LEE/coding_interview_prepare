import heapq
N, K = map(int,input().split(" "))
jewels = [] 
bags = []

for _ in range(N):
    M, V = map(int,input().split(" "))
    jewels.append((M, V))

for _ in range(K):
    C = int(input())
    bags.append(C)

jewels.sort()
bags.sort()

heap = []
idx = 0
result = 0

for bag in bags:
    while idx < len(jewels) and jewels[idx][0] <= bag:
        heapq.heappush(heap, -jewels[idx][1])
        idx += 1
    
    if heap:
        result -= heapq.heappop(heap)

print(result)