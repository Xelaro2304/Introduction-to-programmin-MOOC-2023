# Write your solution here
number = int(input('Please type in a number'))
if number!=1:
    print(number**0+1)
else:  
    print(number)
if number%2 == 0 :
    for i in range (1, number):
        if i%2 == 1:
            print(i)
        else:
            print(i+2)
if number%2 == 1 and number > 1:
    for i in range (1, number-1):
        if i%2 == 1:
            print(i)
        else:
            print(i+2)
    print(number)