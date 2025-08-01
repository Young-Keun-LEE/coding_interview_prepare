import sys
def count(x, y, size):
    global white, blue
    half = size // 2
    
    if is_same(x, y, size) is False:
        count(x, y, half)
        count(x + half, y, half)
        count(x, y + half, half)
        count(x + half, y + half, half)
    
    else:
        if coloredpaper[x][y] == 1:
            blue += 1
            
        else:
            white += 1
    return


def is_same(x, y, size):
    flag = coloredpaper[x][y] 
    for i in range(x, x + size):
        for j in range(y, y + size):
            if flag != coloredpaper[i][j]:
                return False
    return True

input = sys.stdin.readline
coloredpaper = []
N = int(input().strip())
white, blue = 0, 0

for _ in range(N):
    coloredpaper.append(list(map(int, input().strip().split(" "))))

count(0, 0, N)
print(white)
print(blue)