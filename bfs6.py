from collections import deque
N, M = map(int, input().split(" ")) # 0 <= N <= 100,000

visited = [0] * 100001 
queue = deque([(N , 0)])

while queue:
    now, sec = queue.popleft()
    if now == M:
        break

    for next in [now + 1, now - 1, now * 2]:
        if 0 <= next <= 100000 and visited[next] == 0:
            queue.append((next, sec + 1))
            visited[next] = 1

print(sec)