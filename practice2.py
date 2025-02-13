# Greedy algorithm

s = input() #Enter numbers without space

result = 0

for str in s:
    num = int(str) # Convert string to integer
    
    if result <= 1 or num <= 1: # Only if num is 0 '+' is bigger than '*'
        result += int(num)
    else:
        result *= int(num)
        
print(result)
    