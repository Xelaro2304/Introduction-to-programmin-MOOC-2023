# Write your solution here
sentence = input('Please type in a sentence')
print(sentence[0])

for i in range (0, len(sentence)):
    if sentence[i] == ' ':
        print(sentence[i+1])
    