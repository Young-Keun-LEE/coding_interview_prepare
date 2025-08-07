import heapq, sys

N = int(sys.stdin.readline().strip())
heap = []
buffer = []

for _ in range(N):
    num = int(sys.stdin.readline().strip())
    
    if num != 0:
        heapq.heappush(heap, (abs(num), num))

    else:
        if heap:
            buffer.append(heapq.heappop(heap)[1])
        else:
            buffer.append(0)    

sys.stdout.write("\n".join(map(str, buffer)))