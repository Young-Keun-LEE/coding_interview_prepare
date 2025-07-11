import sys
input = sys.stdin.readline
N = int(input())
record = set()

for _ in range(N):
    name, entrance = input().strip().split(" ")
    if entrance == "enter":
        record.add(name)
    elif entrance == "leave":
        record.remove(name)


for name in sorted(record, reverse=True):
    print(name)