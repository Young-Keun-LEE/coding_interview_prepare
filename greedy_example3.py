import sys
#baekjoon 13305
N = int(sys.stdin.readline()) # Input the number of city
length = list(map(int, sys.stdin.readline().split())) # Input length of distance
price =  list(map(int, sys.stdin.readline().split())) # Input price of oil

def next_destination(index):
    for j in range(index + 1, N - 1):
        if price[index] > price[j]:
            return j
    return N - 1

i = 0
result = 0 #Minimum oil price
while i < N - 1:
    j = next_destination(i)
    result += price[i] * sum(length[i:j])
    i = j
    
    
        
sys.stdout.write(str(result))
