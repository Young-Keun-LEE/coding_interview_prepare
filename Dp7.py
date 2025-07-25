N = int(input())
a = 1 # if N == 1
b = 2 # if N == 2

for i in range(3, N + 1):
    a, b = b, (a + b) % 15746

print(a if N == 1 else b)