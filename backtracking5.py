def N_Queen(row):
    global count

    if row == N:
        count += 1
        return

    for c in range(N):
        if col[c] is False:
            if diagonal_1[row - c + (N - 1)] is False and diagonal_2[row + c] is False:
                col[c],diagonal_1[row - c + (N - 1)],diagonal_2[row + c] = True,True,True
                N_Queen(row + 1)
                col[c],diagonal_1[row - c + (N - 1)],diagonal_2[row + c] = False,False,False

count = 0
N = int(input())
col = [False] * N
diagonal_1 = [False] * (2 * N - 1) #row - col + (N - 1) is same
diagonal_2 = [False] * (2 * N - 1) #row + col is same
N_Queen(0)
print(count)