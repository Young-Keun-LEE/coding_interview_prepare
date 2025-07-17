N, M = map(int, input().strip().split())
voca_list = []

for _ in range(N):
    v = input().strip()
    if len(v) >= M:
        voca_list.append(v)

counter = {}
for voca in voca_list:
    if voca in counter:
        counter[voca] += 1
    else:
        counter[voca] = 1

unique_voca = list(counter.keys())
unique_voca.sort(key = lambda x: (-counter[x], x))
print(counter)
print(unique_voca)
