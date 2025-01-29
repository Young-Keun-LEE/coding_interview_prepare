#at some point how many move knight can do
import sys

input = input() #Input current point of knight
current_file_point = ord(input[0]) - ord('a') + 1
current_rank_point = int(input[1])

knight_move = [(-1,2),(-1,-2),(1,2),(1,-2),(2,1),(2,-1),(-2,1),(-2,-1)] #all kind of knight's move
count = 0

for move in knight_move:
    kf = current_file_point + move[0]
    kr = current_rank_point + move[1]
    
    if 1 <= kf <= 8 and 1 <= kr <= 8:
        count += 1
        
 
print(count)

