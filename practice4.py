# Greedy algorithm

n = int(input()) # the number of coin
array = list(map(int, input().split())) # Enter the value of each coin

target = 1 
array.sort()

for coin in array:
    if coin > target:
        break
    else:
        target += coin
        
print(target)