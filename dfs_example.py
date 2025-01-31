import sys
N, M = map(int,input().split()) # N * M matrix 
graph = []
result = 0 
for i in range(N):
    graph.append(list(map(int,input())))

def dfs(x, y):
    if x <= -1 or x >= N or y <= -1 or y >= M: #if x, y location is wrong return False immediately
        return False
    
    if graph[x][y] == 0: #if not visited
        graph[x][y] = 1 #Make visited status
        
        #Search left,right,up,down block    
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    
    return False

for i in range(N): #Do dfs at every point
    for j in range(M):
        if dfs(i, j) == True:
            dfs(i, j)
            result += 1
            
print(result)