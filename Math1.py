import sys
import math
from functools import reduce

input = sys.stdin.readline

distances = []
sum = 0
N = int(input())
prev =  int(input())
current = 0

for i in range(N - 1):
    current = int(input())
    distance = current - prev
    distances.append(distance)
    sum += distance
    prev = current

print(int(sum / reduce(math.gcd, distances)) - N + 1)



