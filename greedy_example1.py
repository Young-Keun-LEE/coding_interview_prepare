import sys

N, K = map(int, input().split()) #Using N of coins make sum K
A = [] #Value of coins
count = 0

for i in range(N):
    A.append(int(sys.stdin.readline()))

A.sort(reverse = True)

for value in A:
    count += K // value
    K %= value

print(count)
    
    