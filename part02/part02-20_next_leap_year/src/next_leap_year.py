# Write your solution here
year = int(input('Year:'))
leap = year

while True:
    leap += 1
    if leap%4 == 0:
        if leap%100 == 0:
            if leap%400 == 0:
                break
        else:
            break
print(f'The next leap year after {year} is {leap}')