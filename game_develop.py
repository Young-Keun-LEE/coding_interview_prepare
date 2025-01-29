import sys #This is coding test book game_develop code

N, M = map(int, sys.stdin.readline().split()) #Input map_size N * M
A, B, direction = map(int, sys.stdin.readline().split()) #Input character's location and direction 
#direction North(0), East(1), South(2), West(3)
area_array = []
for i in range(N): #indicate whether land or ocean
    area_array.append(list(map(int,sys.stdin.readline().split())))
area_array[A][B] = 1
A_move = [-1, 0, 1, 0]
B_move = [0, 1, 0, -1]
count = 1
fail = 0

# Turn left, Go backward
def turn_left():
    global A, B, A_move, B_move, count, direction, fail
    direction -= 1
    
    if direction < 0:
        direction = 3
    
    if area_array[A + A_move[direction]][B + B_move[direction]] == 0:
        area_array[A][B] = 1
        A += A_move[direction]
        B += B_move[direction]
        count += 1
        fail = 0
    else:
        fail += 1


def go_backward():
    global A,B,count,A_move,B_move
    if area_array[A + A_move[direction -2]][B + B_move[direction - 2]] == 0:
        area_array[A][B] = 1
        A += A_move[direction -2]
        B += B_move[direction - 2]
        count += 1
        
    else:
        print(count)
        return



    
while(True):
    turn_left()
    if fail == 4:
        go_backward()
