# Write your solution here
# Write your solution here
def search(dict):
    finnish = input("Search term: ")
    with open(dict) as my_file:
        for line in my_file:
            if finnish in line:
                print (line)



def add(dict):
    finnish = input("The word in Finnish: ")
    english = input("The word in English: ")
    with open(dict, "a") as my_file:
        my_file.write(f"{finnish} - {english}\n")
        print("Dictionary entry added")



def main():
    file = 'dictionay.txt'
    while True:
        print('1 - Add word, 2 Search, 3 Quit: ')
        command = int (input("Function: "))
        if command == 1:
            add(file)
        elif command == 2:
            search(file)
        else:
            print("Bye!")
            break

main()