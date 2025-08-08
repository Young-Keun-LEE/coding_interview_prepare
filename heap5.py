import heapq, sys
data = list(map(int, sys.stdin.read().split())) #Input all of data at once
left_heap, right_heap = [], [] #left_heap is max heap and right_heap is min_heap
idx = 1 #data[0] is The number of test case
output = [] #Accumulate output
medians = [] #For saving median number for each test case

for _ in range(data[0]):
    M = data[idx] #The size of sequence(size is odd number)
    idx += 1
    seq = data[idx: idx + M]
    idx += M
    heapq.heappush(left_heap, -seq[0])
    medians.append(-left_heap[0]) 
    for i in range(1, M):
        if -left_heap[0] < seq[i]:
            heapq.heappush(right_heap, seq[i])

        else:
            heapq.heappush(left_heap, -seq[i])

        if len(left_heap) < len(right_heap): #Maintain length of heap
            heapq.heappush(left_heap, -heapq.heappop(right_heap))
        elif len(left_heap) > len(right_heap) + 1: #Maintain length of heap
            heapq.heappush(right_heap, -heapq.heappop(left_heap))

        if i % 2 == 0:
            medians.append(-left_heap[0])
    
    output.append(str(len(medians)) + "\n")

    for i, val in enumerate(medians, 1):
        output.append(str(val) + ' ')
        if i % 10 == 0:
            output.append("\n")
    output.append("\n")
    left_heap, right_heap, medians = [], [], []

sys.stdout.write(''.join(output))
