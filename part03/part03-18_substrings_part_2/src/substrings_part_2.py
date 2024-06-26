# Write your solution here
# Write your solution here
word = input('Please type in a string')
#print(word[-1])
for i in range (-1, -len(word)-1,-1):
    if i == -1:
        print(word[-1])
    else:
        print(word[i:-1]+f'{word[-1]}')
    #print(i)