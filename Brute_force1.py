chess_board_1 = [['W','B','W','B','W','B','W','B'],
                ['B','W','B','W','B','W','B','W'],
                ['W','B','W','B','W','B','W','B'],
                ['B','W','B','W','B','W','B','W'],
                ['W','B','W','B','W','B','W','B'],
                ['B','W','B','W','B','W','B','W'],
                ['W','B','W','B','W','B','W','B'],
                ['B','W','B','W','B','W','B','W']
                ]

chess_board_2 = [['B','W','B','W','B','W','B','W'],
                ['W','B','W','B','W','B','W','B'],
                ['B','W','B','W','B','W','B','W'],
                ['W','B','W','B','W','B','W','B'],
                ['B','W','B','W','B','W','B','W'],
                ['W','B','W','B','W','B','W','B'],
                ['B','W','B','W','B','W','B','W'],
                ['W','B','W','B','W','B','W','B']
                ]

M, N = map(int, input().split(" ")); # M * N board
board = []
for _ in range(M):
    color = input()
    board.append(list(color)) 


result = 1e9

for padding_x in range(M - 7):
    for padding_y in range(N - 7):
        change_1 = 0
        change_2 = 0
        for i in range (8):
            for j in range(8):
                if board[i + padding_x][j + padding_y] != chess_board_1[i][j]:
                    change_1 += 1
                if board[i + padding_x][j + padding_y] != chess_board_2[i][j]:
                    change_2 += 1

        result = min(change_1, change_2, result)
print(result)


