import sys

def matrix_pow(A, B, N): # A ^ B
    if B == 1:
        return modulo_matrix(A, N)
    half = matrix_pow(A, B // 2, N)
    res = calculate_square(half, N)

    if B % 2 == 1:
        res = calculate_multiple(res, A, N)
    return res
        
def calculate_square(C, N): # Calculate C ^ 2, N is size of matrix
    result = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                result[i][j] += C[i][k] * C[k][j]
    
    return modulo_matrix(result, N)

def calculate_multiple(A, B, N): # if A and B is different calculate A * B, both size is N
    result = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                result[i][j] += A[i][k] * B[k][j]
    
    return modulo_matrix(result, N)    

def modulo_matrix(A, N):
    for i in range(N):
        for j in range(N):
            A[i][j] %= 1000
    return A

    
input = sys.stdin.readline
print = sys.stdout.write

A = []
N, B = map(int, input().strip().split(" ")) # matrix A is N by N matrix and calculate A ^ B

for _ in range(N):
    A.append(list(map(int, input().strip().split(" "))))

C = matrix_pow(A, B, N)
print('\n'.join(' '.join(map(str, row)) for row in C))

