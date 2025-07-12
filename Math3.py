is_prime = [True] * 1000001
is_prime[0] = False
is_prime[1] = False

# Find prime number less than 1,000,001
for i in range(2, int(1000001 ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i ** 2, 1000001, i):
            is_prime[j] = False

def find_Goldbach(n):
    count = 0
    for i in range(2, n  // 2 + 1):
        if is_prime[i] is True and is_prime[n - i] is True:
            count += 1
    return count  

T = int(input())
Numbers = []
for _ in range(T):
    Numbers.append(int(input()))

for number in Numbers:
    print(find_Goldbach(number))



          





