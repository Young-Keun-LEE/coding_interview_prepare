from itertools import combinations

n = int(input()) #Board is n * n matrix
teachers = []
spaces = []
board = []


for i in range(n):
    
    board.append(list(input().split()))   
    for j in range(n):
        if board[j] == 'T':
            teachers.append((i, j))
            
        if board[j] == 'X':
            spaces.append((i, j))


def detect(x, y, direction):
    if direction == 0:
        while x < n:
            if board[x][y] == 'O':
                return False
            if board[x][y] == 'S':
                return True
            x += 1
        return False
    
    elif direction == 1:
        while 0 <= x:
            if board[x][y] == 'O':
                return False
            if board[x][y] == 'S':
                return True
            x -= 1
        return False    
    
    elif direction == 2:
        while y < n:
            if board[x][y] == 'O':
                return False
            if board[x][y] == 'S':
                return True            
            y += 1
        return False
    
    else:
        while 0 <= y:
            if board[x][y] == 'O':
                return False
            if board[x][y] == 'S':
                return True            
            y -= 1
        return False

def process(): #If find student return True
    for tx, ty in teachers:
        for i in range(4):
            if detect(tx, ty, i):
                return True
    return False
        
    
cases = combinations(spaces, 3)

flag = False

for case in cases:
    for x, y in case:
        board[x][y] = 'O'
        
    if process() is False:
        print("YES")
        flag = True
        break
    
    for x, y in case:
        board[x][y] = 'X'

if flag is False:
    print("NO")
        
