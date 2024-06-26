# Write your solution here

def store_personal_data(person: tuple):
    existing = []
    new = ''
    with open ("people.csv", "w") as file:
        person_data = []
        person_data.append(person[0])
        person_data.append(str(person[1]))
        person_data.append(str(person[2]))
        line = ';'.join(person_data) + '\n'
        file.write(line)