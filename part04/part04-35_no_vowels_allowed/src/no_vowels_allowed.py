# Write your solution here
def no_vowels (word):
    new_word = ''
    for i in word:
        if i != "a" and i != "e" and i != "i" and i != "o" and i != "u":
            new_word += i
    return new_word
