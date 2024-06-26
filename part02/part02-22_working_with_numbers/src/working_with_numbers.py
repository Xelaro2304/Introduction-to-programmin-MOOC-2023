# Write your solution here
count = 0
add = 0
pnum = 0
nnum = 0
print('Please type in integer numbers. Type in 0 to finish.')
while True:
    number = int(input('Number:'))
    add += number
    if number == 0:
        break
    elif number > 0:
        pnum += 1
    else:
        nnum += 1
    count += 1
print(f'Numbers typed in {count}')
print(f'The sum of the numbers is {add}')
print(f'The mean of the numbers is {add/count}')
print(f'Positive numbers {pnum}')
print(f'Negative numbers {nnum}')
