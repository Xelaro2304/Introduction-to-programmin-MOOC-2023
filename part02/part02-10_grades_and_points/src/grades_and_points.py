# Write your solution here
points = int(input())

if points<0 or points>100:
    print('impossible!')
elif 0<= points <=49:
    print(f'Grade: fail')
elif 50<= points <=59:
    print(f'Grade: 1')
elif 60<= points <=69:
    print(f'Grade: 2')
elif 70<= points <=79:
    print(f'Grade: 3')
elif 80<= points <=89:
    print(f'Grade: 4')
elif 90<= points <=100:
    print(f'Grade: 5')
