def is_valid(i, j, num):
    if num not in rows[i] and num not in cols[j] and num not in squares[(i // 3) * 3 + (j // 3)]:
        return True
    
    else:
        return False
    
def backtrack(idx):

    if idx == len(blank_space):
        return True
    
    i, j = blank_space[idx]
    
    for num in range(1, 10):
        if is_valid(i, j, num):
            board[i][j] = num
            rows[i].add(num)
            cols[j].add(num)
            squares[(i // 3) * 3 + (j // 3)].add(num)

            if backtrack(idx + 1):
                return True
            
            board[i][j] = 0
            rows[i].remove(num)
            cols[j].remove(num)
            squares[(i // 3) * 3 + (j // 3)].remove(num)
    return False

board = [] # Board size is 9 * 9 
blank_space = []

for _ in range(9):
    board.append(list(map(int, input().split(" "))))

rows = [set() for _ in range(9)]
cols = [set() for _ in range(9)]
squares = [set() for _ in range(9)]

for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            blank_space.append((i, j))
        else:
            rows[i].add(board[i][j])
            cols[j].add(board[i][j])
            squares[3 * (i // 3) + (j // 3)].add(board[i][j])

backtrack(0)

for i in range(9):
    for j in range(9):
        print(board[i][j], end = " ")
    print()

