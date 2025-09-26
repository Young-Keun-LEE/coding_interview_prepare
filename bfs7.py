from collections import deque
T = int(input())
result = []
for _ in range(T):
    limit = int(input())
    x, y = map(int, input().split(" "))
    now = (x, y, 0)
    x, y = map(int, input().split(" "))
    dest = (x, y)
    visited = [[0] * limit for _ in range(limit)] 
    queue = deque([now])
    dx = [1, 2, 1, 2, -1, -2, -1, -2]
    dy = [2, 1, -2, -1, 2, 1, -2, -1]


    while queue:
        cx, cy, cnt = queue.popleft()
        if cx == dest[0] and cy == dest[1]:
            result.append(cnt)
            break
        
        for i in range(8):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < limit and 0 <= ny <limit and visited[nx][ny] == 0:  
                queue.append((nx, ny, cnt + 1))
                visited[nx][ny] = 1

for r in result:
    print(r)

