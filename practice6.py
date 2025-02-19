s = input()
half = len(s) // 2
length = len(s)
sum1 = 0
sum2 = 0
for i in range(0, half):
    sum1 += int(s[i])

for i in range(half, length):
    sum2 += int(s[i])
    
if sum1 == sum2:
    print("LUCKY")
else:
    print("READY")