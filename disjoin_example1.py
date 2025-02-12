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
        
n, m = map(int, input().split()) # There are team 0 to n and m is the number of operator
parent = [0] * (n + 1)

for i in range(n + 1): # Initialize the parent table with the parent referencing itself 
    parent[i] = i
    
for i in range(m): #Enter operators from user
    op, a, b = map(int, input().split())
    
    if op == 0: #If op is 0 union teams
        union_parent(parent, a, b)
    
    elif op == 1: #If op is 1 check a and b are both same team
        
        if find_parent(parent, a) == find_parent(parent, b):
            print("YES")
            
        else:
            print("NO")
            
