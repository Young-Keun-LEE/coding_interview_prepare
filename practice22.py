def find_fix_point(array, start, end):
    mid = (start + end) // 2

    if start > end:
        return -1

    if array[mid] < mid:
        return find_fix_point(array, mid + 1, end)
    
    elif array[mid] > mid:
        return find_fix_point(array, start, mid - 1)
    
    else:
        return mid

n = int(input())
array = list(map(int, input().split()))
print(find_fix_point(array, 0, n - 1))

