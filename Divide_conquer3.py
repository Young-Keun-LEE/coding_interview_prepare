import sys
def is_uniform(x, y, size):
    flag = bitmap[x][y]
    for i in range(x, x + size):
        for j in range(y, y + size):
            if flag != bitmap[i][j]:
                return False
    return True

def make_tree(x, y, size):
    global tree
    half = size // 2
    
    if is_uniform(x, y, size) is False:
        tree.append("(")
        make_tree(x, y, half)
        make_tree(x, y + half, half)
        make_tree(x + half, y, half)
        make_tree(x + half, y + half, half)
        tree.append(")")
    
    else:
        if bitmap[x][y] == 1:
            tree.append("1")
        else:
            tree.append("0")
    return

input = sys.stdin.readline
bitmap = []
tree = []
N = int(input().strip())

for _ in range(N):
    bitmap.append(list(map(int, input().strip())))

make_tree(0, 0, N)
print("".join(tree))

