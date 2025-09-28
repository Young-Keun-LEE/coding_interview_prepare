from collections import deque

def bfs():
    queue = deque([(1, 0)]) #(location, time)
    while queue:
        now, time = queue.popleft()
        for num in dice:
            next = now + num
            if next == 100:
                time += 1
                return time
            
            if next in move:
                next = move[next]

            if 0 < next <= 100 and not visited[next]:
                queue.append((next, time + 1))
                visited[next] = 1

N, M = map(int, input().split(" "))
visited = [0] * 101
move = {}
dice = [1, 2, 3, 4, 5, 6]

for _ in range(N):
    x, y = map(int, input().split(" "))
    move[x] = y

for _ in range(M):
    u, v = map(int, input().split(" "))
    move[u] = v



print(bfs())