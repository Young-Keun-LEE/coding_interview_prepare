import math
m, n = map(int, input().split()) # Find prime number in range m , n

prime_num = [True] * 1000001
prime_num[1], prime_num[0] = False, False
for i in range(2, int(math.sqrt(1000000)) + 1):
    if prime_num[i]:
        j = 2
        while i * j <= 1000000:
            prime_num[i * j] = False
            j += 1
    
for i in range(m, n + 1):
    if prime_num[i]:
        print(i)

