mod = 1000000007
def pow_matrix(A, n): #Calculate A ^ n
    if n == 1:
        return [[x % mod for x in row] for row in A]
    
    half = pow_matrix(A, n // 2) #A ^ (n // 2)
    if n % 2 == 1:
        return mult_matrix(mult_matrix(half,half), A)
    
    return mult_matrix(half,half)

def mult_matrix(A, B):
    if len(A[0]) != len(B):
        raise ValueError("Can't multiply matrices: incompatible dimensions")
    C = [[0] * len(B[0]) for _ in range(len(A))] # C is A * B
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % mod
    
    return C

def fibo(n): #Calculate (A ^ n) * B
    if n == 0:
        return 0
    
    A = [[1, 1], [1, 0]]
    B = [[1], [0]]
    result = mult_matrix(pow_matrix(A, n), B)
    return result[1][0]

n = int(input())
print(fibo(n) % 1000000007)