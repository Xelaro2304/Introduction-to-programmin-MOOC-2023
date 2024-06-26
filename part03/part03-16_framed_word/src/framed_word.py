# Write your solution here
word = input('Word:')
space = int((28-len(word))/2)
print('*'*30)
#print(f'{3*"*"}')
if len(word)%2 == 0:
   print(f'*{space*" "}{word}{space*" "}*')
else:
   print(f'*{space*" "}{word}{space*" "} *')
print('*'*30)