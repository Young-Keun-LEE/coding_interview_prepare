import sys
input = sys.stdin.readline
N, M = map(int, input().split(" "))
S = set()
count = 0

for _ in range(N):
    S.add(input())
    
for _ in range(M):
    str = input()
    if str in S:
        count += 1

print(count)    