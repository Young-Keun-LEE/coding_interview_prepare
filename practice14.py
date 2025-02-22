# n = int(input()) #The number of operand
# numbers = list(map(int, input().split()))
# add, sub, mul, div = map(int, input().split()) #The number of operator

# max_value = float('-inf')
# min_value = float('inf')

# def dfs(index, now):
#     global add, sub, mul, div
#     global max_value, min_value
    
#     if index == n:
#         max_value = max(max_value, now)
#         min_value = min(min_value, now) 
    
#     else:
#         if add > 0:
#             add -= 1
#             dfs(index + 1, now + numbers[index])
#             add += 1
    
#         if sub > 0:
#             sub -= 1
#             dfs(index + 1, now - numbers[index])
#             sub += 1

#         if mul > 0:
#             mul -= 1
#             dfs(index + 1, now * numbers[index])
#             mul += 1
        
#         if div > 0:
#             div -= 1
#             dfs(index + 1, int(now / numbers[index])) # C++14 standard
#             div += 1


# dfs(1, numbers[0])

# print(max_value)
# print(min_value)

from itertools import permutations

n = int(input()) #The number of operand
numbers = list(map(int, input().split()))
operators = []
add, sub, mul, div = map(int, input().split()) #The number of operator

for _ in range(add):
    operators.append(0)
    
for _ in range(sub):
    operators.append(1)
    
for _ in range(mul):
    operators.append(2)
    
for _ in range(div):
    operators.append(3)   

max_value = float('-inf')
min_value = float('inf')

cases = permutations(operators, n - 1)



for case in cases:
    
    now = numbers[0]
    
    for i in range(n - 1):
        
        if case[i] == 0:
            now += numbers[i + 1]
        
        elif case[i] == 1:
            now -= numbers[i + 1]
            
        elif case[i] == 2:
            now *= numbers[i + 1]
            
        elif case[i] == 3:
            now = int(now / numbers[i + 1])
    
    max_value = max(max_value, now)
    min_value = min(min_value, now)
    
print(max_value)
print(min_value)
