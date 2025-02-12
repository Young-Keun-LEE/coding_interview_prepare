def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    
    if a < b:
        parent[b] = a
    
    else:
        parent[a] = b
        
v, e = map(int, input().split()) #Enter the number of vertex and edge
edges = [] #For saving edges
parent = [0] * (v + 1)

for i in range(1, v + 1): # Initialize the parent table with the parent referencing itself 
    parent[i] = i    

for _ in range(e):
    a, b, c = map(int, input().split()) #Connect a and b, cost is c
    edges.append((c, a, b))

edges.sort() #Sort edges by cost
last = 0 #For saving last edge's cost
result = 0 #Calculate cost

for edge in edges: #Do kruskal's algorithm
    
    c, a, b = edge
    
    if find_parent(parent, a) != find_parent(parent, b): #If edge doesn't make cycle, connect two vertexs
        union_parent(parent, a, b)
        result += c
        last = c

print(result - last)
