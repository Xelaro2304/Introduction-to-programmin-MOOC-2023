# Write your solution here
list=[]
print(f'The list is now {list}')
choice=input('a(d)d, (r)emove or e(x)it:')
while choice != 'x':
    if choice == 'd':
        list.append(len(list)+1)
    elif choice == 'r':
        list.pop((-1))
    print(f'The list is now {list}')
    choice=input('a(d)d, (r)emove or e(x)it:')
print('Bye!')