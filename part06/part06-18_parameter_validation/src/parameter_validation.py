# Write your solution here
def new_person(name: str, age: int):
    if len(name) > 40 or 0 > age or age > 150 or ' ' not in name or name == '':
        raise ValueError('An error occurred')
    else:
        return name, age