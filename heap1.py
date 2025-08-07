import sys
# import heapq
def insert(heap, value): # heap is min_heap
    heap.append(value)
    idx = len(heap) - 1
    while idx > 0:
        parent = (idx - 1) // 2
        if heap[parent] <= heap[idx]:
            break
        else:
            heap[parent], heap[idx] = heap[idx], heap[parent]
            idx = parent

def pop(heap):
    if not heap:
        return None
    if len(heap) == 1:
        return heap.pop()
    root = heap[0]
    heap[0] = heap.pop()
    idx = 0
    while True:
        left_child = 2 * idx + 1
        right_child = 2 * idx + 2
        smallest = idx

        if left_child < len(heap) and heap[left_child] <= heap[smallest]:
            smallest = left_child

        if right_child < len(heap) and heap[right_child] <= heap[smallest]:
            smallest = right_child
            
        if smallest == idx:
            break

        heap[smallest], heap[idx] = heap[idx], heap[smallest]
        idx = smallest
    return root
        
N = int(sys.stdin.readline().strip())
heap = []
# heapq.heapify(heap)
output = []

for _ in range(N):
    num = int(sys.stdin.readline().strip())
    if num == 0:
        if heap:
            output.append(str(-pop(heap)))
        else:
            output.append("0")
    else:
        insert(heap, -num)  
    
sys.stdout.write("\n".join(output))