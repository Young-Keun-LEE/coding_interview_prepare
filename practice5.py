n, m = map(int, input().split()) # n is the number of bowling ball and m is maximum weight of ball
weights = list(map(int, input().split())) # Enter weight of ball
count = [0] * (m + 1)

for weight in weights:
    count[weight] += 1

result = n * (n - 1) // 2

for i in range(1, m + 1):
    if count[i] > 0:
        result -= count[i] * (count[i] - 1) // 2
    
print(result)

