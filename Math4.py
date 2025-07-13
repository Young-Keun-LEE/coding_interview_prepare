import math
A, B = map(int, input().split()) # A / B
C, D = map(int, input().split()) # C / D

# Calculate A / B + C / D = F / G 

lcm = int(math.lcm(B, D))
G = lcm
F = A * int(lcm / B) + C * int(lcm / D)

gcd = int(math.gcd(F, G))
print(f"{F // gcd} {G // gcd}")


