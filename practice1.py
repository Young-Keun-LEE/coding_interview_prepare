#Greedy algorithm

N = int(input()) # N is the number of adventurers
array = list(map(int, input().split())) # Adventurer' s degree of fear
count = 0 # The number of team member
result = 0 # Final result
array.sort()
for x in array:
    count += 1
    if count >= x:
        count = 0
        result += 1
        


print(result)