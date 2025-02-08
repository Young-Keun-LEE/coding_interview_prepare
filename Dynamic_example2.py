N = int(input()) #The number of hut
array = list(map(int, input().split())) #The number of food each hut

# Maximize the number of food
d = [0] * N
d[0] = array[0]
d[1] = max(array[1] ,array[0])

for i in range(2, N):
    d[i] = max(d[i - 1], d[i - 2] + array[i])


print(d[N - 1])