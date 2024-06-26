# Write your solution here
word1 = input()
word2 = input()
lnght1 = len(word1)
lnght2 = len(word2)

if lnght1 < lnght2:
    print(f'{word2} is longer')
elif lnght2 < lnght1:
    print(f'{word1} is longer')
else:
    print('The strings are equally long')
