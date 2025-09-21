from collections import deque
def bfs(x, y):
    queue = deque([(x, y)])
    visited[y][x] = 1
    while queue:
        cx, cy = queue.popleft()
        for idx in range(4):
            nx = cx + dx[idx]
            ny = cy + dy[idx]
            if 0<= nx < M and 0<= ny < N and visited[ny][nx] == 0 and (nx, ny) in cabbage:
                queue.append((nx, ny))
                visited[ny][nx] = 1
    return
  
T = int(input()) # The number of test case
result = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for _ in range(T):
    cabbage = set()
    M, N, K = map(int, input().split(" "))
    visited = [[0] * M for _ in range(N)]
    cnt = 0

    for _ in range(K):
        x, y = map(int, input().split(" "))
        cabbage.add((x, y))
    
    for cx, cy in cabbage:
        if visited[cy][cx] == 0:
            bfs(cx, cy)
            cnt += 1
    
    result.append(cnt)

for r in result:
    print(r)

