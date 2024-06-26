# write your solution here
def read_fruits():
    with open("fruits.csv") as new_file:
        fruit_dictionary = {}
        for line in new_file:
            line = line.replace("\n", "")
            fruits = line.split(";")
            fruit_name = fruits[0]
            fruit_price = fruits[-1]
            fruit_dictionary[fruit_name] = float(fruit_price)
        return fruit_dictionary

read_fruits()