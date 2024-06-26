# Write your solution here
import json

def print_persons(filename: str):
    with open(filename) as my_file:
        data = my_file.read()
    persons = json.loads(data)
    for i in persons:
        for key, value in i.items():
            if key == "age":
                print(f'{value} years ', end='')
            elif key == 'hobbies':
                print(f'({", ".join(value)})')
            else:
                print(f'{value} ', end='')
#print_persons('file1.json')