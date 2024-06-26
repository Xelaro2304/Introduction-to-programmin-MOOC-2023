# Write your solution here
word = input('Please type in a word')
character = input('Please type in a substring')
deleted = len(word[0:word.find(character)+len(character)])
if character in word:
    word = word[deleted:]
if character in word:
    print(f'The second occurrence of the substring is at index {word.find(character)+deleted}.')
else:
    print('The substring does not occur twice in the string.')