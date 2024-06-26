# Write your solution here
number = int(input("Please type in a number"))

for first in range (1, number + 1):
    for second in range (1, number + 1):
        print(f'{first} x {second} = {first*second}')