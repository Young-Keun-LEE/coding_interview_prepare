import sys
print = sys.stdout.write
count = 0

def hanoi_tower(N, FROM, TO, VIA):
    global count

    if N == 1: # Base case (if N is 1 just move from -> to)
        print(f'{FROM} {TO}\n' )
        count += 1

    else: # Recursive case(step 1, 2, 3)
        hanoi_tower(N - 1, FROM, VIA, TO) #step1
        print(f'{FROM} {TO}\n') #step2
        count += 1
        hanoi_tower(N - 1,VIA, TO, FROM) #step3

N = int(input())
print(str(2 ** N - 1) + "\n")
hanoi_tower(N, 1, 3, 2)