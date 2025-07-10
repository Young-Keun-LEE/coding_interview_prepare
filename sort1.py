N = int(input())
box = [[] for _ in range(51)]
for i in range(N):
    voca = input()
    len_voca = len(voca)
    if voca not in box[len_voca]:
        box[len_voca].append(voca)

for i in range(1, 51):
    box[i].sort()
    if box[i] is not None:
        for j in range(len(box[i])):
            print(box[i][j])
