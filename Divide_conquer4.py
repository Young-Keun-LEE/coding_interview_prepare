import sys
def is_uniform(x, y, size):
    compare = paper[y][x]
    for i in range(y, y + size):
        for j in range(x, x + size):
            if compare != paper[i][j]:
                return False
    return True

def count_paper(x, y, size):
    global count_1, count_2, count_3

    if is_uniform(x, y, size):
        if paper[y][x] == -1:
            count_1 += 1
        elif paper[y][x] == 0:
            count_2 += 1
        elif paper[y][x] == 1:
            count_3 += 1
    else:
        partial = size // 3
        new_x = [x, x + partial, x + partial * 2]
        new_y = [y, y + partial, y + partial * 2]
        for nx in new_x:
            for ny in new_y:
                count_paper(nx, ny, partial)

input = sys.stdin.readline
count_1 = 0 # Count the number of uniform paper with -1 
count_2 = 0 # Count the number of uniform paper with 0
count_3 = 0 # Count the number of uniform paper with 1
paper = []
N = int(input().strip())
for _ in range(N):
    paper.append(list(map(int, input().strip().split(" "))))
count_paper(0, 0, N)
print(count_1, count_2, count_3 ,sep = "\n")

