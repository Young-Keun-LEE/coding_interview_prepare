import sys
input = sys.stdin.readline

T = int(input())
result = []
for i in range(T):
    ps = list(input().strip())
    open = 0
    close = 0
    flag = False
    for _ in range(len(ps)):
        if ps.pop() == "(":
            open += 1
        else:
            close += 1
        if close < open:
            result.append("NO")
            flag = True
            break
    if not flag: 
        if close == open:
            result.append("YES")
        else:
            result.append("NO")

for r in result:
    sys.stdout.write(r + "\n")
