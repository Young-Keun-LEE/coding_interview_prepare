from itertools import combinations
n, m = map(int, input().split()) # Map size is N * N and I should choose M of chicken store
house = []
chicken = []
for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        if data[j] == 1:
            house.append((i, j))
        elif data[j] == 2:
            chicken.append((i, j))

candidates = combinations(chicken, m)

def get_sum(candidate):
    sum = 0
    for hx, hy in house:
        distance = 1e9
        for cx, cy in candidate:
            distance = min(distance, abs(hx - cx) + abs(hy - cy))
        sum += distance
    
    return sum

result = 1e9
for candidate in candidates:
    result = min(result, get_sum(candidate))

print(result)
            
            