N, S = map(int, input().split(" ")) 
numbers = list(map(int, input().split(" ")))
pt1 = pt2 = 0 # Initalize pointers
min_len = N + 1
current_sum = numbers[0]

while pt1 < N:
    if current_sum >= S:
        length = pt2 - pt1 + 1
        min_len = min(length, min_len)
        current_sum -= numbers[pt1]
        pt1 += 1
    else:
        pt2 += 1
        if pt2 == N:
            break
        current_sum += numbers[pt2]

if min_len > N:
    print(0)
else:
    print(min_len)