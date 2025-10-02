from collections import deque
N, M = map(int, input().split(" "))
wall = [[] for _ in range(N)]
visited = [[[0, 0] for _ in range(M)] for _ in range(N)]
move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

for i in range(N):
    row = input()
    for num in row:
        wall[i].append(int(num))

queue = deque([(0, 0, 0, 1)]) # (row, column, break?, distance)
visited[0][0][0] = 1

while queue:
    row, col, brk, dist = queue.popleft()
    if row == N - 1 and col == M - 1: # If arrive at goal
        print(dist)
        exit(0)

    for dr, dc in move:
        nr = row + dr
        nc = col + dc
        if 0 <= nr < N and 0 <= nc < M and visited[nr][nc][brk] == 0:
            if wall[nr][nc] == 1: # If meet wall
                if brk == 1: # Already break wall once
                    continue
                else: # Can break the wall!
                    queue.append((nr, nc, 1, dist + 1))
                    visited[nr][nc][1] = 1
                
            else: # If it is not wall
                queue.append((nr, nc, brk, dist + 1))
                visited[nr][nc][brk] = 1
                
if visited[N - 1][M - 1][0] == 0 and visited[N - 1][M - 1][1] == 0:
    print(-1)


