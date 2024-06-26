# Write your solution here
letter1 = input()
letter2 = input()
letter3 = input()

if letter1 < letter2 < letter3 or letter3 < letter2 < letter1:
    print(f'The letter in the middle is {letter2}')
elif letter2 < letter3 < letter1 or letter1 < letter3 < letter2:
    print(f'The letter in the middle is {letter3}')
elif letter3 < letter1 < letter2 or letter2 < letter1 < letter3:
    print(f'The letter in the middle is {letter1}')