n = int(input()) #board size is n * n
k = int(input()) #k is the number of apple
data = [[0] * (n + 1) for _ in range(n + 1)] #Map data
info = [] #direction info
for _ in range(k):
    row, col = map(int, input().split())
    data[row][col] = 1

l = int(input()) #l is the number of changing direction

for _ in range(l): #Enter direction infomations
    time, char = input().split()
    info.append((int(time), char))


dx = [0, 1, 0, -1] #east, south, west, north each
dy = [1, 0, -1, 0]

def turn(direction, c):
    if c == 'L':
        direction = (direction - 1) % 4
    elif c == 'D':
        direction = (direction + 1) % 4
    return direction
        
def simulation():
    x, y = 1, 1 #Starting point
    data[x][y] = 2
    direction = 0 #First direction is east
    time = 0
    index = 0 #For check turning time
    q = [(x, y)] #First one is tail
    while True:
        time += 1
        nx = x + dx[direction]
        ny = y + dy[direction]
        
        if nx < 1 or n < nx or ny < 1 or n < ny or data[nx][ny] == 2: #If not satisfy conditions
            break
        
        x = nx
        y = ny
        
        if data[nx][ny] != 1: #If there is not apple
            px, py = q.pop(0) #Remove tail
            data[px][py] = 0
            data[nx][ny] = 2
            q.append((nx, ny))
        
        else:
            data[nx][ny] = 2
            q.append((nx, ny))
        
        
        if index < l and time == info[index][0]: #If should turn direction
            direction = turn(direction, info[index][1])
            index += 1
    
    return time          
                
        
print(simulation())
    