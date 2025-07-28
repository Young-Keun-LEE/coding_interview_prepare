import sys
input = sys.stdin.readline

N = int(input()) #The number of electric wire
wire = []

for _ in range(N):
    A, B = map(int, input().split(" "))
    wire.append((A, B))

sequence = []
for A, B in sorted(wire):
    sequence.append(B)

dp = [1] * N 

for i in range(1, N):
    for j in range(i):
        if sequence[j] < sequence[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(N - max(dp))


