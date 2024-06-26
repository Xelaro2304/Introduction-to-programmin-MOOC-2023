# Write your solution here

import re


def find_words(search_term: str):
    words=[]
    found_words = []
    with open ("words.txt") as file:
        for line in file:
            line = line.strip()
            words.append(line)
    for word in words:
        if search_term.startswith('*'):
            if word.endswith(search_term.replace('*','')):
                found_words.append(word)
        elif search_term.endswith('*'):
            if word.startswith(search_term.replace('*','')):
                found_words.append(word)
        elif '.' in search_term:
            if re.search(search_term, word) and len(word) == len(search_term):
                found_words.append(word)
        else:
            if search_term == word:
                found_words.append(word)
    return found_words

#find_words('reson*')