# Write your solution here
import fractions


def fractionate(number: int):
    fraction_list= []
    for i in range (number):
        fraction_list.append(fractions.Fraction(1, number))
    return fraction_list