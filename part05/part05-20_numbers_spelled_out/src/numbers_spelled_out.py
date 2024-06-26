# Write your solution here
def dict_of_numbers():
    under20 = {
        '0':"zero",
        '1': "one", 
        '2': "two", 
        '3': "three", 
        '4': "four", 
        '5': "five",
        '6': "six", 
        '7': "seven", 
        '8': "eight", 
        '9': "nine", 
        '10': "ten",
        '11': "eleven", 
        '12': "twelve", 
        '13': "thirteen", 
        '14': "fourteen",
        '15': "fifteen", 
        '16': "sixteen", 
        '17': "seventeen", 
        '18': "eighteen", 
        '19': "nineteen"
    }
    tens = {
        '2': "twenty", 
        '3': "thirty", 
        '4': "forty", 
        '5': "fifty",
        '6': "sixty", 
        '7': "seventy", 
        '8': "eighty", 
        '9': "ninety"
    }
    dictionary = {}
    for i in range (0, 100):
        if i < 20:
            dictionary[i] = under20[str(i)]
        else:
            written_word = str(i)
            first = written_word[0]
            second = written_word[1]
            if second == '0':
                dictionary[i] = tens[first]
            else:
                dictionary[i] = f'{tens[first]}-{under20[second]}'
    return dictionary
