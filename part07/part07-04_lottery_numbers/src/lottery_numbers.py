# Write your solution here
import random

def lottery_numbers(amount: int, lower: int, upper: int):
    number_pool = list(range(lower,upper+1))
    numbers = random.sample(number_pool, amount)
    numbers = sorted(numbers)
    return numbers

#lottery_numbers((1,1,10))