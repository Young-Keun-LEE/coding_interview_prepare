import sys
import math

input = sys.stdin.readline

T = int(input())
result = []

for _ in range(T):
    N, M = map(int, input().strip().split(" "))
    result.append(math.comb(M, N))

print("\n".join(map(str,result)))
