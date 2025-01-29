import sys
#baekjoon 2941
voca = list(input()) #input voca from user
croatian_word = ('c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=') #dictionary of croatian word
count_word = 0 #count the number of word
word = None
index = 0 #index of array

while index < len(voca):
    word = voca[index]
    
    if index < len(voca) - 1:
        word = voca[index] + voca[index + 1]
    
    if word in croatian_word:
        index += 2
        count_word += 1
        continue
    
    if index < len(voca) - 2:
        word = voca[index] + voca[index + 1] + voca[index + 2]
    
    if word in croatian_word:
        index += 3
        count_word += 1
        continue
    
    count_word += 1
    index += 1


print(count_word)
