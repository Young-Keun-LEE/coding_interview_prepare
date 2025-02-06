d = [0] * 100 #Memorize duplicated value

def fibo(N): #Calculate N of fibornacci's number // Top - Down
    if N == 1 or N == 2: #1st and 2nd number is 1
        return 1
    
    if d[N] != 0:
        return d[N]
    else:
        d[N] = fibo(N - 1) + fibo(N - 2)
        return d[N]

# print(fibo(10))

d[1] = 1
d[2] = 1
N = 99

for i in range(3, N + 1): # Bottom - Up
    d[i] = d[i - 1] + d[i - 2]

print(d[99])