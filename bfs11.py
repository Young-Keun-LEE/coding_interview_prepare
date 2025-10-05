# Solve 0 - 1 bfs problem
from collections import deque 

INF = float("inf")
max_limit = 100000
n, k = map(int, input().split(" ")) # n is start point, k is destination
distance = [INF] * (max_limit + 1) # Recode shortest time to arrive at node
queue = deque([n])
distance[n] = 0

while queue:
    now = queue.popleft()
    next = now * 2 # if go now * 2
    if 0 <= next <= max_limit and distance[next] > distance[now]:
            distance[next] = distance[now] # * 2 move doesn't need any time!
            queue.appendleft(next)

    for dx in [1, -1]: #if go + 1 , - 1
        next = now + dx
        if 0 <= next <= max_limit and distance[next] > distance[now] + 1:
                distance[next] = distance[now] + 1
                queue.append(next)

print(distance[k])
