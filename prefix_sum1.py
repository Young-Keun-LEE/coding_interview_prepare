N, K = map(int, input().split(" "))
celsius = []
celsius = list(map(int, input().split(" ")))

i = 0 # First pointer
j = i + K # Second pointer

current_sum = sum(celsius[i : j])
max_val = current_sum

while j < N:
    difference = celsius[j] - celsius[i]
    current_sum += difference
    max_val = max(max_val, current_sum)
        
    i += 1
    j += 1

print(max_val)