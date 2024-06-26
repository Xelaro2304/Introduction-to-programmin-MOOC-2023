# Write your solution here
from datetime import datetime, timedelta

#filename = 'first_of_may.txt'
#start_date = '1.5.2020'
#how_long = 1


filename = input('Filename: ')
start_date = input('Starting date')
how_long = int(input('How many days'))

now = datetime.strptime(start_date, '%d.%m.%Y')
log_end = now + timedelta(days=how_long-1)

total = 0
log={}


with open(filename, "w") as clean:
    pass

print('Please type in screen time in minutes on each day (TV computer mobile): ')
with open(filename, "a") as file:
    for i in range (how_long):
        log_date = now + timedelta(days=i)
        screen_time= input(log_date.strftime('%d.%m.%Y')+': ')
        log[log_date.strftime('%d.%m.%Y')] = '/'.join(screen_time.split(' '))
        for j in screen_time.split(' '):
            total += int(j)
    file.write(f'Time period: {now.strftime("%d.%m.%Y")}-{log_end.strftime("%d.%m.%Y")}\n')
    file.write(f'Total minutes: {total}\n')
    file.write(f'Average minutes: {total/how_long}\n')


    for key, value in log.items():
        file.write(f'{key}: {value}\n')
