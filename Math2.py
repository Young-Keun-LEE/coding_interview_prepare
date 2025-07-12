A, B = map(int, input().split()) #Calculate LCM of A and B
gcd = 0
C, D = A, B

while True:
    if C < D:
        D = D % C
    else:
        C = C % D
    
    if C == 0:
        gcd = D
        break

    if D == 0:
        gcd = C
        break


print(int(A * B / gcd))
