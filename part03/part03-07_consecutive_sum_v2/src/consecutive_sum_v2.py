# Write your solution here
limit = int(input())
add=1
suma=1
operation=''

while add < limit:
    suma+=1
    add+=suma
    operation = operation + f'+ {suma} '

print(f'The consecutive sum: 1 {operation}= {add}')
