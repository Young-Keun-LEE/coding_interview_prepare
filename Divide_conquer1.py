def fast_pow(a, b, c):
    if b == 0:
        return 1
    
    if b % 2 == 0:
        return (fast_pow(a, b // 2, c) % c) ** 2 % c
    
    else:
        return (fast_pow(a, b // 2, c) % c) ** 2 * a % c

A, B, C = map(int, input().split())
print(fast_pow(A, B, C))

