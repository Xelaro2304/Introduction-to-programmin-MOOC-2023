# Write your solution here
story = ''
repeat=''
while True:
    word = input()
    if word == repeat:
        break
    elif word != 'end':
        story += word + ' '
        repeat = word
    else:
        break
print(story)