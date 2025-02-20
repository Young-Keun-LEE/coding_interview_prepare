from collections import deque
n, k = map(int, input().split())
graph = []
data = []
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] != 0:
            data.append((graph[i][j], 0, i, j))
            
    
target_time, target_x, target_y = map(int, input().split())
data.sort()
q = deque(data)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while q:
    virus, time, x, y = q.popleft()
    if time == target_time:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus, time + 1, nx, ny))

print(graph[target_x - 1][target_y - 1])
                