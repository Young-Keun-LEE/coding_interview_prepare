import sys
input = sys.stdin.readline

N = int(input())
original_dots = list(map(int, input().split(" ")))
unique_sorted_dots = sorted(list(set(original_dots)))

coordinate_map = {value: idx for idx, value in enumerate(unique_sorted_dots)}

for dot in original_dots:
    sys.stdout.write(str(coordinate_map[dot]) + " ")
