S = input()
subString = set()

for i in range(len(S) + 1):
    for j in range(len(S) + 1):
        subString.add(S[i:j])

subString.remove("")
print(len(subString))
