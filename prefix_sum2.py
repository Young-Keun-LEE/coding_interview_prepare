import sys
input = sys.stdin.readline
print = sys.stdout.write

S = input().strip()
q = int(input())
result = []
prefix = [[0] * (len(S) + 1) for _ in range(26)] #prefix[alphabet_index][index]

for i in range(1, len(S) + 1):
    for j in range(26):
        prefix[j][i] = prefix[j][i - 1]
    prefix[ord(S[i - 1]) - 97][i] += 1

for _ in range(q):
    command = list(input().strip().split(" "))
    char = ord(command[0]) - 97
    l, r = map(int, command[1:])
    result.append(prefix[char][r + 1] - prefix[char][l])

print("\n".join(map(str,result)))
