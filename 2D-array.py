N = int(input())
square = [[0] * 100 for _ in range(100)]

for i in range(N):
    left_margin, bottom_margin = map(int, input().split(" "))
    for j in range(left_margin, left_margin + 10):
        for k in range(bottom_margin, bottom_margin + 10):
            square[j][k] = 1

sum = 0
for i in range(100):
    for j in range(100):
        sum += square[i][j]
print(sum)
