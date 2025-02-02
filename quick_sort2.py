#Make quick_sort algorithm using python's adventage
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8] #Array example

def quick_sort2(array):
    if len(array) <= 1: #if array has only one element, return array
        return array
    
    pivot = array[0]
    test_array = array[1:]
    
    left_array = [x for x in test_array if x <= pivot]
    right_array = [x for x in test_array if x > pivot]
    
    return quick_sort2(left_array) + [pivot] + quick_sort2(right_array)
    

print(array)
print(quick_sort2(array))