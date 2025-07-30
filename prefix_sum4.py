from math import comb
N, M = map(int, input().split(" "))
A = list(map(int, input().split(" ")))
count = [0] * M
count[0] = 1
sum = 0

for i in range(len(A)):
    sum += A[i]
    count[sum % M] += 1

result = 0
for n in count:
    result += comb(n , 2)

print(result)