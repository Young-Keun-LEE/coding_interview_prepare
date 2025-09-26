from collections import deque
def is_ripe():
    for i in range(n):
        for j in range(m):
            if box[i][j] == 0:
                return False
    return True

m, n = map(int, input().split(" "))
box = []
tomato = []
move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

for _ in range(n):
    row = list(map(int, input().split(" ")))
    box.append(row)

for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            tomato.append((i, j, 0))

visited = [[0] * m for _ in range(n)]
queue = deque()

for x, y, time in tomato:
    queue.append((x, y, time))
    visited[x][y] = 1
    
while queue:
    x, y, time = queue.popleft()
    for dx, dy in move:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and box[nx][ny] == 0:
            queue.append((nx, ny, time + 1))
            visited[nx][ny] = True
            box[nx][ny] = 1


if any(0 in row for row in box):
    print("-1")
else:
    print(time)


