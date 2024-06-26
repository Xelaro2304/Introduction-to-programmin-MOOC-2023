# Write your solution here
limit = int(input('Upper limit'))
base = int(input())
n = 1
power = 1

while power <= limit:
    print(power)
    power = base ** n
    n += 1