# write your solution here
sentence = input('Write text: ')
word_list = sentence.split(' ')
dictionary = []
with open("wordlist.txt") as thessaurus:
    for line in thessaurus:
        line = line.replace("\n", "")
        dictionary.append(line)

for word in word_list:
    if word.lower() in dictionary:
        print(f'{word} ', end="")
    else:
        print(f'*{word}* ', end="")
print()