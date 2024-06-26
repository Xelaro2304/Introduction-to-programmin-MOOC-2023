# Write your solution here
import random

def roll(die: str):
    if die == 'A':
        choice = 3, 3, 3, 3, 3, 6
    if die == 'B':
        choice = 2, 2, 2, 5, 5, 5
    if die == 'C': 
        choice = 1, 4, 4, 4, 4, 4
    return random.choice(choice)


def play(die1: str, die2: str, times: int):
    player_1_result = 0
    player_2_result = 0
    tie = 0
    for i in range (times):
        throw1 = roll(die1)
        throw2 = roll(die2)
        if throw1 > throw2:
            player_1_result += 1
        if throw1 < throw2:
            player_2_result += 1
        if throw1 == throw2:
            tie += 1
    return player_1_result, player_2_result, tie


