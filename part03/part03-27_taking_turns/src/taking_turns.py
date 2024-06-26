# Write your solution here
number = int(input('Please type in a number'))
for i in range (0, number//2):
    print(i+1)
    print(number-i)
if number%2 !=0 :
    print(number//2+1)
