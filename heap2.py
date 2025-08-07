import sys, heapq

buffer = []
N = int(sys.stdin.readline().strip())
heap = []
heapq.heapify(heap)
for _ in range(N):
    num = int(sys.stdin.readline().strip())
    if num == 0:
        if heap:
            buffer.append(heapq.heappop(heap))
        else:
            buffer.append(0)

    else:
        heapq.heappush(heap, num)

print("\n".join(map(str, buffer)))