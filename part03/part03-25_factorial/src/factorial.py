# Write your solution here
number = int(input('Please type in a number:'))
while number > 0:
    factorial = 1
    for i in range (number, 1, -1):
        factorial *= i
    print(f'The factorial of the number {number} is {factorial}')
    number = int(input('Please type in a number:'))
print('Thanks and bye!')