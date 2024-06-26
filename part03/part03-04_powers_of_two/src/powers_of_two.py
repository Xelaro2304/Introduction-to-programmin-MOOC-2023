# Write your solution here
limit = int(input('Upper limit'))

n = 1
power = 1

while power <= limit:
    print(power)
    power = 2 ** n
    n += 1