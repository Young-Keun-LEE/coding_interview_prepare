array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8, 2, 14, 4, 7, 2, 1]

def quick_sort(array, start, end):
    
    pivot = start #Make frist element pivot
    left = start + 1
    right = end
    
    while left <= right: #Execute the code only if left < right
               
        while left <= end: #Find larger element than pivot's value
            if array[left] > array[pivot]:
                break
            left += 1
        
        while right > pivot: #Find smaller element than pivot's value
            if array[right] < array[pivot]:
                break
            right -= 1
            
        if right < left: #If two pointers cross, switch pivot's value with right's value
            array[pivot], array[right] = array[right], array[pivot]
            quick_sort(array, start, right - 1)
            quick_sort(array, right + 1, end)
        
        else: #If not switch left's value with right's
            array[left], array[right] = array[right], array[left]
        
    
print(array)
quick_sort(array, 0, len(array) - 1)
print(array)