# Write your solution here
students = int(input('How many students on the course'))
size = int(input('Desired group size'))

if students%size != 0:
    group = students//size+1
else:
    group = students/size
print(f'Number of groups formed: {int(group)}')

