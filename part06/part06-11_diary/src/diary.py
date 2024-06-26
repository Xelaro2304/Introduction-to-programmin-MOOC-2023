# Write your solution here

def read_diary(diary):
    with open(f"{diary}") as file:
        print('Entries: ')
        for line in file:
            print(line.strip())



def add_diary(diary):
    with open(f"{diary}", "a") as file:
        entry = input("Diary entry: ")
        file.write(f'{entry}\n')
    print("Diary saved")

def diary_modifier(diary_file):
    while True:
        print("1 - add an entry, 2 - read entries, 0 - quit")
        to_do = int(input("Function: "))
        if to_do == 0:
            print("Bye now!")
            break
        if to_do == 1:
            add_diary(diary_file)
        if to_do == 2:
            read_diary(diary_file)



diary_modifier("diary.txt")