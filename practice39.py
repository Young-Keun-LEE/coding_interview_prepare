import sys
from collections import deque
input = sys.stdin.readline

for tc in range(int(input())):
     n = int(input())
     graph = [[False] * (n + 1) for _ in range(n + 1)]
     indegree = [0] * (n + 1)
     data = list(map(int, input().split()))
     
     for i in range(n):
          for j in range(i + 1, n):
               graph[data[i]][data[j]] = True
               indegree[data[j]] += 1
     
     m = int(input())
     for _ in range(m):
         a, b = map(int, input().split())
         if graph[a][b] == True:
               graph[a][b] = False
               graph[b][a] = True
               indegree[a] += 1
               indegree[b] -= 1
         else:
              graph[b][a] = False
              graph[a][b] = True
              indegree[a] -= 1
              indegree[b] += 1
     
     q = deque()
     
     for i in range(1, n + 1):
          if indegree[i] == 0:
               q.append(i)
     
     cycle = False
     certain = False
     result = []
     
     for i in range(n):
          if len(q) == 2:
               certain = True
               break
          if len(q) == 0:
               cycle = True
               break
          node = q.popleft()
          result.append(node)
          
          for j in range(1, n + 1):
               if graph[node][j] == True:
                    graph[node][j] = False
                    indegree[j] -= 1
                    if indegree[j] == 0:
                         q.append(j)
                         
     if cycle:
          print("IMPOSSIBLE")
          
     elif certain:
          print("?")
          
     else:
          for i in result:
               print(i, end = " ")
          print()