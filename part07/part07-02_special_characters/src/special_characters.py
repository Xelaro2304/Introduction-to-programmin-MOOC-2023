# Write your solution here
import string

def separate_characters(my_string: str):
    a = ''
    b = ''
    c = ''
    for i in range (0, len(my_string)):
        letter = my_string[i]
        if letter in string.ascii_letters:
            a += letter
        elif letter in string.punctuation:
            b += letter
        else:
            c += letter
    return (a,b,c)
