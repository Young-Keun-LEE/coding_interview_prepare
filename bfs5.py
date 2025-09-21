from collections import deque
def bfs(x, y): # dfs algorithm starting at (x, y)
    queue = deque([(x, y, 1)])
    visited[x][y] = 1 # starting point

    while queue:
        cx, cy, dist = queue.popleft()
        for idx in range(4):
            nx = cx + dx[idx]
            ny = cy + dy[idx]
            if 0<= nx < N and 0<= ny < M and visited[nx][ny] == 0 and maze[nx][ny] == 1:              
                if nx == N - 1 and ny == M - 1:
                    return dist + 1
                
                else:
                    queue.append((nx, ny, dist + 1))
                    visited[nx][ny] = 1
        

N, M = map(int, input().split(" "))
maze = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
visited = [[0] * M for _ in range(N)]


for _ in range(N):
    line = input()
    row = [int(n) for n in line]
    maze.append(row)

print(bfs(0, 0)) # Maze starts at (0, 0)