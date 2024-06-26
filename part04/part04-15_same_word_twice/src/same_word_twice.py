# Write your solution here
list=[]
while True:
    word=input('Word:')
    if word not in list:
        list.append(word)
    else:
        print(f'You typed in {len(list)} different words')
        break