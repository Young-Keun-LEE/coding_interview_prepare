import heapq
n = int(input())
decks = []
for _ in range(n):
    heapq.heappush(decks, int(input()))
compare = 0

for _ in range(n - 1):
    a = heapq.heappop(decks)
    b = heapq.heappop(decks)
    compare += a + b
    heapq.heappush(decks, a + b)
    
print(compare)