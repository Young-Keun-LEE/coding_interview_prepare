import sys
from collections import Counter
input = sys.stdin.readline
voca_list = []

N, M = map(int, input().strip().split())

for _ in range(N):
    v = input().strip()
    length = len(v)

    if length >= M:
        voca_list.append(v)

counter = Counter(voca_list)

unique_voca = list(counter.keys())

unique_voca.sort(key=lambda x: (- counter[x], -len(x), x))

for v in unique_voca:
    sys.stdout.write(v + "\n")

