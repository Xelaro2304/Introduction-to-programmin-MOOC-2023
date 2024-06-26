# Write your solution here
import random, string

def generate_password(length: int):
    password = ''
    for i in range (length):
        password += random.choice(string.ascii_lowercase)
    return password
#generate_password(4)