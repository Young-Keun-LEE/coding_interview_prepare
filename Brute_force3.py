N = int(input()) # N <= 10000

no = 0 # Refer order of number to find
current = 0 # Exhaustively search for the desired number using brute-force

while True:
    current += 1
    if str(current).find("666") != -1:
        no += 1
        if no == N:
            break
        
print(current)
    