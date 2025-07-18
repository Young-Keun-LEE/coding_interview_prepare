import sys

def stars(N):

    if N == 1:
        return ['*']
    
    prev = stars(N // 3)
    now = []
    
    for i in range(3):
        if i == 1:
            for line in prev:
                now.append(line + " " * (N // 3) + line)
        else:
            for line in prev:
                now.append(line * 3)

    return now


N = int(input()) # N is 3 ^ n
print('\n'.join(stars(N)))

