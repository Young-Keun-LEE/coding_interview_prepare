import sys
N = int(sys.stdin.readline()) #Input number of people
P = list(map(int, sys.stdin.readline().split())) #Array of spent time by person
P.sort() #Sort array P
time = 0 #Spent time
for i in range(len(P)):
    for j in range(i + 1):
        time += P[j]
sys.stdout.write(str(time))       