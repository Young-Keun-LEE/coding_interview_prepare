import heapq
# Among N ^ 2 numbers, find N th biggest number

heap = []
N = int(input())

for _ in range(N):
    row = list(map(int, input().split(" ")))
    for i in range(N):
        if len(heap) == N:
            heapq.heappushpop(heap, row[i])
        else:
            heapq.heappush(heap, row[i])
            
print(heapq.heappop(heap))



