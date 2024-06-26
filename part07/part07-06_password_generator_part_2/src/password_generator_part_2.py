# Write your solution here
from random import choice, randint
from string import ascii_lowercase, digits

#def generate_strong_password(length: int, number: bool, special: bool):
#    password = ''
#    menu = string.ascii_lowercase
#    number_string = string.digits
#    special_string = '!?=+-()#'
#    again = True
#    number_count = 0
#    special_count = 0
#    while again:
#        if number and special:
#            menu += number_string + special_string
#            for i in range (length):
#                character = random.choice(menu)
#                password += character
#                if character in number_string:
#                    number_count += 1
#                if character in special_string:
#                    special_count += 1
#            if special_count > 0 and number_count > 0:
#                again = False
#        elif number:
#            menu += number_string
#            for i in range (length):
#                character = random.choice(menu)
#                password += character
#                if character in number_string:
#                    number_count += 1
##            if number_count > 0:
#                again = False
##        elif special:
#            menu += special_string
#            for i in range (length):
#                character = random.choice(menu)
#                password += character
#                if character in special_string:
#                    special_count += 1
#            if special_count > 0:
#                again = False
##        else:
#            for i in range (length):
#                character = random.choice(menu)
#                password += character
##
##    return password



def generate_strong_password(length: int, numbers: bool, special_characters: bool):
    special_chars = "!?=+-()#"
    # One letter at beginning of the password
    passwd = choice(ascii_lowercase)
    choice_set = ascii_lowercase
 
    # If numbers is wanted, add at least one number
    if numbers:
        passwd = add_character(passwd, digits)
        choice_set += digits
 
    # same for special characters
    if special_characters:
        passwd = add_character(passwd, special_chars)
        choice_set += special_chars
 
    # build the rest of the password from the whole set
    while (len(passwd) < length):
        passwd = add_character(passwd, choice_set)
 
    return passwd
 
# Add a random character from the given set either
# at the beginning or end of the string
def add_character(passwd: str, characters):
    character = choice(characters)
    if randint(1,2) == 1:
        return character + passwd
    else:
        return passwd + character
