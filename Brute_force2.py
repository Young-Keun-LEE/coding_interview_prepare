N = int(input()) #Kilogram of sugar
ref = N // 5
result = -1
for i in range(ref, -1, -1): # i is the number of 5kg bag
    remainder = N - i * 5
    if remainder % 3 == 0:
        result = i + remainder // 3
        break

print(result)
    