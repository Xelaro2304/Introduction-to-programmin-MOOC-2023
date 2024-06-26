# Write your solution here
iter = int(input('How many items:'))
list = []
for i in range(0,iter):
    item_i = int(input(f'Item{i+1}'))
    list.append(item_i)
print(list)