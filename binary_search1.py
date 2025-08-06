from bisect import bisect_left, bisect_right

def binary_search(A, element): #Doing binary search for finding element in A array
    length = len(A)
    start = 0
    end = length - 1
    mid = (start + end) // 2

    while start <= end:

        if A[mid] == element:
            return mid

        elif A[mid] < element:
            start = mid + 1

        elif A[mid] > element:
            end = mid - 1
        
        mid = (start + end) // 2
    
    return -1

N = int(input())
A = list(map(int, input().split(" ")))
A.sort()
M = int(input())
find = list(map(int, input().split(" ")))

for f in find:
    if bisect_left(A, f) != bisect_right(A, f):
        print("1")
    else:
        print("0")