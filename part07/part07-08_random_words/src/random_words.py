# Write your solution here
import random

def words(n: int, beginning: str):
    words = []
    with open('words.txt') as file:
        for line in file:
            word_filter = line.strip()
            if word_filter.startswith(beginning):
                words.append(word_filter)
    return random.sample(words, n)