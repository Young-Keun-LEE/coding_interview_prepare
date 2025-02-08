N, M = map(int, input().split()) # N is value of money, M is required sum of money
# Calculate minimum number of money to make value of M
array = []
for i in range(N):
    array.append(int(input()))
    
d = [10001] * (M + 1)
d[0] = 0
for value in array:
    for i in range(value, M + 1):
        d[i] = min(d[i - value] + 1, d[i])

if d[i] >= 10001:
    print(-1)
else:
    print(d[M])
