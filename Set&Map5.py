NA, NB = map(int, input().split()) #The number of element in set A, B

A = set(map(int, input().split()))
B = set(map(int, input().split()))

count = 0

for element in A.symmetric_difference(B):
    count += 1

print(count)

