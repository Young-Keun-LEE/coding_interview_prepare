str = input()
count = 0
sum = 0
str = sorted(str)
for s in str:
    if s.isdigit():
        count += 1
        sum += int(s)
        
str.append(sum)   
for i in range(count,len(str)):
    print(str[i], end = "")
    