# Write your solution here
name1 = input()
age1 = int(input())
name2 = input()
age2 = int(input())

if age1 > age2:
    print(f'The elder is {name1}')
elif age1 < age2:
    print(f'The elder is {name2}')
else:
    print(f'{name1} and {name2} are the same age')