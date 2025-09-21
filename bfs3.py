from collections import deque
def bfs(x, y): # bfs algorithm starting at (x, y)
    queue = deque([(x, y)])
    visited[x][y] = True
    cnt = 1

    while queue:
        cx, cy = queue.popleft()
        for idx in range(4):
            nx = cx + dx[idx]
            ny = cy + dy[idx]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0 and graph[nx][ny] == 1:
                queue.append((nx, ny))
                visited[nx][ny] = 1
                cnt += 1
    
    return cnt

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
n = int(input())
graph = []
visited = [[0] * n for _ in range(n)]
result = []

for i in range(n):
    row = input()
    arr = [int(ch) for ch in row]
    graph.append(arr)

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0 and graph[i][j] == 1:
            result.append(bfs(i, j))

result.sort()
print(len(result))
for num in result:
    print(num)


