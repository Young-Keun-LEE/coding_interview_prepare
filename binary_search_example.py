def binary_search(array, target, start, end):
    
    mid = (start + end) // 2
    
    if start > end:
        return None
    
    if array[mid] == target:
        return mid
    
    elif array[mid] < target:
        start = mid + 1
        return binary_search(array, target, start, end)
        
    else:
        end = mid - 1
        return binary_search(array, target, start, end)
    
N = int(input()) #The number of gadget
array = list(map(int, input().split()))

array.sort()

M = int(input()) #The number of required gadget
require = list(map(int, input().split()))

for i in require:
    if binary_search(array, i, 0, N - 1) != None:
        print("yes", end = " ")
    else:
        print("no", end = " ")


# for i in require: 
#     if i in array:
#         print("yes", end = " ")
#     else:
#         print("no", end = " ")

