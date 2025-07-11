numbers = list(input())
numbers = list(map(int, numbers))
numbers.sort(reverse=True)

for number in numbers:
    print(number, end = "")   