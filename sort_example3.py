N, K = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse = True)

def swap_element(index, A, B): 
    A[index], B[index] = B[index], A[index]

for i in range(K): #Exchange elements between arrays A and B K times
    if A[i] < B[i]: #Exchange elements only if A[i] is smaller than B[i]
        swap_element(i, A, B)

sum = 0

for i in range(N):
    sum += A[i] 

print(sum)  