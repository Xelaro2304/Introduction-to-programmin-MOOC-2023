# Write your solution here
def read_input(text, a, b):
    while True:
        try:
            integer = int(input(f"{text}"))
        except ValueError:
            integer = a-1
        if integer < a or integer > b:
            print(f'You must type in an integer between {a} and {b}')
            continue
        else:
            return integer
    
#read_input('asda ', 5, 10)