# Greedy algorithm

s = input() # Enter number without space
result = 0 # Count the number of fliping

compare = s[0] # first number of string

for i in range(len(s) - 1):
    if s[i] == compare and s[i + 1] != compare: # If number is changed, increase result by 1
        result += 1

print(result)