line = input()
seg = list(line.split("-"))
result = 0
sum = 0
for num in seg[0].split("+"):
    result += int(num)

for i in range(1, len(seg)):
    for num in seg[i].split("+"):
        sum += int(num)
    result -= sum
    sum = 0
print(result)