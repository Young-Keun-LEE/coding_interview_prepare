def get_prime(N): # Make prime number list using sieve of eratosthenes
    is_prime = [True] * (N + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(N ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, N + 1, i):
                is_prime[j] = False

    prime = []
    for i in range(2, N + 1):
        if is_prime[i]:
            prime.append(i)
    return prime

N = int(input())
prime = get_prime(N)
start = end = 0
current_sum = 0
cnt = 0

while start < len(prime):
    
    if current_sum == N:
        cnt += 1
        current_sum -= prime[start]
        start += 1
    elif current_sum < N:
        if end == len(prime):
            break
        current_sum += prime[end]
        end += 1
    else:
        current_sum -= prime[start]
        start += 1

print(cnt)