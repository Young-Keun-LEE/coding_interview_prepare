def backtrack(i, val, add, sub, mul, div):
    global max, min
    op = 0

    if i == N:
        if val > max:
            max = val

        if val < min:
            min = val

        return
    
    if add != 0:
        backtrack(i + 1, val + operand[i], add - 1, sub, mul, div)

    if sub != 0:
        backtrack(i + 1, val - operand[i], add, sub - 1, mul, div)

    if mul != 0:
        backtrack(i + 1, val * operand[i], add, sub, mul - 1, div)

    if div != 0:
        if val > 0:
            backtrack(i + 1, val // operand[i], add, sub, mul, div - 1)
        else:
            backtrack(i + 1, -(-val // operand[i]), add, sub, mul, div - 1)
        
max, min = map(int,(-1e9,1e9))
N = int(input())
operand = list(map(int, input().split(" ")))
add, sub, mul, div = map(int, input().split(" ")) #The number of (+), (−), (×), (÷), in that order.
backtrack(1, operand[0], add, sub, mul, div)
print(max, min, end = "\n")


