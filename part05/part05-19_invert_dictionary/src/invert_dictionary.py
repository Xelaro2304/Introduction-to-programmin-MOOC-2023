# Write your solution here
def invert(dictionary: dict):
    dictionary2 = {}
    for key, value in dictionary.items():
        dictionary2[value] = key
    dictionary.clear()
    for key, value in dictionary2.items():
        dictionary[key] = value
    a= 0