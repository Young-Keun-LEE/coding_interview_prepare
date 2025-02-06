def sequential_search(n, target, array):
    for i in range(n):
        if target == array[i]:
            return i + 1
    return None

print("Enter the number of elements to generate followed by a space and the string to search for.")
input_data = input().split()
N = int(input_data[0])
target = input_data[1]

print("Enter the strings as many as the number of elements mentioned above. Separate them with a single space.")
array = input().split()

print(sequential_search(N, target, array))