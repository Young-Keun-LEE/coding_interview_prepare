n, c = map(int, input().split())
houses = []
for _ in range(n):
    houses.append(int(input()))
houses.sort()

start = 0
end = houses[n - 1] - houses[0]
result = -1

while start <= end:
    mid = (start + end) // 2
    count = 1
    prev = houses[0]
    for i in range(1, n):
        if houses[i] - prev >= mid:
            prev = houses[i] 
            count += 1
        
    if count < c:
        end = mid - 1
        
    else:
        start = mid + 1
        result = mid

print(result)