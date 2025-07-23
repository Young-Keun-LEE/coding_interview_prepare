N = int(input())  # Read the number of elements
numbers = list(map(int, input().split()))  # Read the list of integers

current_sum = numbers[0]  # Initialize the current subarray sum
max_sum = numbers[0]  # Initialize the maximum subarray sum

for pt in range(1, N):
    # If adding the current number improves the sum, extend the subarray
    if current_sum + numbers[pt] >= numbers[pt]:
        current_sum += numbers[pt]
    else:
        # Otherwise, start a new subarray from the current number
        current_sum = numbers[pt]
    
    # Update the maximum subarray sum found so far
    max_sum = max(max_sum, current_sum)

print(max_sum)  # Print the result
