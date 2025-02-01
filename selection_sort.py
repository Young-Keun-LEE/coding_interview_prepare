array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8] # sort array with selection sort algorithm

for i in range(len(array)): 
    min_index = i
    for j in range(i, len(array), 1):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]
    
print(array)

