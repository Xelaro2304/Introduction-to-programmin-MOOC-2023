# Write your solution here
def factorials(n: int):
    factorials_dictionary = {}
    temp = 1
    for i in range (1, n+1):
        for j in range (1, i+1):
            temp *= j
            factorials_dictionary [i] = temp
        temp= 1
    return factorials_dictionary

