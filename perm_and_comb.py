import itertools

data = [1, 2, 3, 4]

print("---------------------------- permutation result")
for x in itertools.permutations(data, 2):
    print(list(x))
    
print("---------------------------- combination result")    
for x in itertools.combinations(data, 2):
    print(list(x))