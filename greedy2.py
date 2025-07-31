import sys  
input = sys.stdin.readline

N = int(input().strip())
meeting = []
for _ in range(N):
    start, end = map(int, input().strip().split(" "))
    meeting.append((start, end))

meeting = sorted(meeting, key = lambda x: (x[1], x[0]))


count = 0
prev_end = 0
for m in meeting:
    start, end = m
    if prev_end <= start:
        prev_end = end
        count += 1
print(count)