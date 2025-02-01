array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8] #Sort array using insertion_sort

for i in range(1, len(array), 1):
    for j in range(i, 0, -1):
        if array[j] < array[j - 1]:
            array[j - 1], array[j] = array[j], array[j - 1]
        else:
            break
print(array)
