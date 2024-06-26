# Write your solution here
def histogram(word: str):
    letter_list = {}
    for letter in word:
        if letter not in letter_list:
            letter_list[letter] = '*'
        else:
            letter_list[letter] += '*'
    for key, value in letter_list.items():
        print (f'{key} {value}')
        