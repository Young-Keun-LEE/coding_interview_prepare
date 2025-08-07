from bisect import bisect_left
N = int(input())
A = list(map(int, input().split(" ")))

temp = [] # list for calculating length of LIS
for e in A:
    idx = bisect_left(temp, e)
    if idx == len(temp):
        temp.append(e)
    else:
        temp[idx] = e

print(len(temp))
