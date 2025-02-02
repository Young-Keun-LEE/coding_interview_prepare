N = int(input()) #Baekjoon 2750
array = [] #For saving input value
for i in range(N):
    array.append(int(input()))
    
array.sort()
for i in range(N):
    print(array[i])