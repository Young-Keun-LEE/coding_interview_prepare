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
        

n, target = map(int, input().split())

array = list(map(int, input().split()))

result = binary_search(array, target, 0, n - 1)

if result == None:
    print("There is no element")

else:
    print(result + 1)
        
    