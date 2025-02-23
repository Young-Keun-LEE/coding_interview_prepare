n = int(input())
locations = list(map(int, input().split()))

locations.sort()
if n % 2 == 0:
    print(locations[n // 2 - 1])
else:
    print(locations[n // 2])