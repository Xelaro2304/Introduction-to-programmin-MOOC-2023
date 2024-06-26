# Write your solution here
def search(provisional):
    name = input("name: ")
    if name in provisional:
        print(provisional[name])
    else:
        print("no number")




def add(provisional):
    name = input("name: ")
    number = input("number: ")
    provisional[name] = number
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