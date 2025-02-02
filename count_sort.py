array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8, 2, 14, 4, 7, 2, 1]

count_array = [0] * (max(array) + 1)# Make array for counting the number of element

for i in range(len(array)):
    count_array[array[i]] += 1

for i in range(len(count_array)):
    for j in range(count_array[i]):
        print(i, end = ' ')