# Write your solution here
import datetime

dayp = int(input('Day: '))
monthp = int(input('Month: '))
yearp = int(input('Year: '))

Birthyear = datetime.datetime(yearp, monthp, dayp)
difference = datetime.datetime(1999, 12, 31) - Birthyear 

if difference.days > 0:
    print(f'You were {difference.days} days old on the eve of the new millennium.')
else:
    print(f"You weren't born yet on the eve of the new millennium.")