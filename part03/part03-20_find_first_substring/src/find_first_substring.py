# Write your solution here
word = input('Please type in a word')
character = input('Please type in a character')
substring = ''
index = word.find(character)
if character in word:
    substring += word[index:index+3]
if len(substring) == 3:
    print(substring)
