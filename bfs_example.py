from collections import deque
N, M = map(int, input().split()) # Graph's size is N by M
graph = []
for i in range(N): # Input graph
    graph.append(list(map(int, input())))
    
dx = [0, 0, -1, 1] # Top, bottom, left, right
dy = [-1, 1, 0, 0]


def bfs(x,y):
    queue = deque() #Make queue
    queue.append((x,y))
    
    while queue:
        x, y = queue.popleft() 
                
        for i in range(4): # Search 4 directions top, bottom, left, right
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx <= -1 or N <= nx or ny <= -1 or M <= ny: # If index is out of array, ignore it !!
                continue
            
            if graph[nx][ny] == 0: #If location is wall, do not go
                continue
            
            if graph[nx][ny] == 1: #If first visited, calculate distance
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
    
    return graph[N - 1][M - 1]
            
            
            
            
        
    
print(bfs(0,0))