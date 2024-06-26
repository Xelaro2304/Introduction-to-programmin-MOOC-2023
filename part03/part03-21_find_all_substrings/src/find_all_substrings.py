# Write your solution here
word = input('Please type in a word')
character = input('Please type in a character')
substring = ''
while len(word) >= 3:
    index = word.find(character)
    if character in word[0]:
        substring = word[index:index+3]
    if len(substring) == 3:
        print(substring)
    word = word[1:]
    substring = ''