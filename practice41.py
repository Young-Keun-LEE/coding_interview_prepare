#The password consists of L different lowercase alphabetic characters and must contain at least one vowel (a, e, i, o, u) and at least two consonants.
from itertools import combinations

l, c = map(int, input().split())
character = list(input().split())
vowel = ['a', 'e', 'i', 'o', 'u']
character.sort()

for case in list(combinations(character, l)):
    vowel_count = 0
    consonant_count = 0
    
    for char in case:
        if char in vowel:
            vowel_count += 1
        else:
            consonant_count += 1
    
    if vowel_count >= 1 and consonant_count >= 2:
        print("".join(case))
                 