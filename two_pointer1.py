N = int(input())
numbers = list(map(int, input().split(" ")))
numbers.sort() # Sorting numbers
pt1 = 0 # 1st pointer
pt2 = N - 1 # 2nd pointer
answer = numbers[pt1] + numbers[pt2]
candidate = [numbers[0], numbers[N - 1]] # Save answer pointers

while pt1 < pt2:
    current = numbers[pt1] + numbers[pt2]
    if current == 0:
        answer = current
        candidate[0] = numbers[pt1]
        candidate[1] = numbers[pt2]
        break
    elif abs(current) < abs(answer):
        answer = current
        candidate[0] = numbers[pt1]
        candidate[1] = numbers[pt2]

    if current > 0: # Move pointer
        pt2 -= 1
    if current < 0:
        pt1 += 1

    
print(*candidate)
