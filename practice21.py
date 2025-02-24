# from bisect import bisect_left, bisect_right

# def count_element(array, x):
#     left = bisect_left(array, x)
#     right = bisect_right(array, x)
    
#     if right - left == 0:
#         return - 1
    
#     else:
#         return right - left

# n , x = map(int, input().split())
# numbers = list(map(int, input().split()))

# print(count_element(numbers, x))

def count_element(array , x, start, end): # How many x are in array
    if find_left(array, x, start, end) == -1:
        return -1
    else:
        return find_right(array, x , start, end) - find_left(array, x , start, end) + 1

def find_left(array, x, start, end):
    
    if start > end :
        return -1
    
    mid = (start + end) // 2
    
    if array[mid] > x:
        return find_left(array, x, start, mid - 1)
    
    elif array[mid] < x:
        return find_left(array, x , mid + 1, end)
        
    else:
        if array[mid - 1] < array[mid]:
            return mid
        else:
            return find_left(array, x, start, mid - 1)
        
def find_right(array, x, start, end):
    
    if start > end :
        return -1
    
    mid = (start + end) // 2
    
    if array[mid] > x:
        return find_right(array, x, start, mid - 1)
    
    elif array[mid] < x:
        return find_right(array, x , mid + 1, end)
        
    else:
        if array[mid + 1] > array[mid]:
            return mid
        else:
            return find_right(array, x , mid + 1, end)
            
n , x = map(int, input().split())
numbers = list(map(int, input().split()))

print(count_element(numbers, x, 0, len(numbers) - 1))