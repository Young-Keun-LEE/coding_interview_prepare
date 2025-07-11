N = int(input())
bucket = {value: idx for idx, value in enumerate(list(map(int, input().split(" "))))}
M = int(input())
test = list(map(int, input().split(" ")))

for i in test:
    if i in bucket:
        print("1", end = " ")
    else:
        print("0", end = " ")