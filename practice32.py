import heapq
INF = int(1e9)
dx = [-1, 1, 0, 0]#Top, Bottom, Left, Right
dy = [0, 0, -1, 1]

t = int(input())
for _ in range(t): # Loop for each test case
    n = int(input()) # Map is n * n matrix
    graph = []
       
    for i in range(n):
        graph.append(list(map(int, input().split())))
    
    distance = [[INF] * n for _ in range(n)]
    
    x, y = 0, 0
    q = heapq()
    q.heapqpush((graph[0][0], 0, 0))
    
    while q:
        dist, a, b = q.heapqpop() 
        if distance[a][b] < 
        for i in range(4):
            x += dx[i]
            y += dy[i]       


    
    