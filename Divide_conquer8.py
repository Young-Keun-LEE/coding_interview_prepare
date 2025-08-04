mod = 1_000_000_007
def mod_pow(a, b): #Calculate a ^ b
    result = 1
    while b > 0:
        if b % 2 == 1:
            result *= a
            result %= mod
        a **= 2
        a %= mod
        b //= 2
    return result

def mod_factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
        result %= mod
    return result

def mod_inverse(a): #Find inverse of a for mod p
    return mod_pow(a, mod - 2)

N, K = map(int, input().split(" ")) #Calculate combination(N, K) module 1000000007
answer = mod_factorial(N) * mod_inverse(mod_factorial(K)) % mod * mod_inverse(mod_factorial(N - K)) % mod

print(answer)