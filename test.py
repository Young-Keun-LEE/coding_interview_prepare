import heapq

array = [(1, 2), (1, 100) ,(3, 0)]
heapq.heapify(array)
print(heapq.heappop(array))
print(heapq.heappop(array))
print(heapq.heappop(array))