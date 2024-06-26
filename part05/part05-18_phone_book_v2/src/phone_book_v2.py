# Write your solution here
def search(provisional):
    name = input("name: ")
    if name in provisional:
        for number in provisional[name]:
            print(number)
    else:
        print("no number")




def add(provisional):
    name = input("name: ")
    number = input("number: ")
    if name not in provisional:
        provisional[name] = [number]
    else:
        provisional[name].append(number)
    print("ok!")


def main():
    directory = {}
    while True:
        command = int (input("command (1 search, 2 add, 3 quit): "))
        if command == 1:
            search(directory)
        elif command == 2:
            add(directory)
        else:
            print("quitting...")
            break

main()