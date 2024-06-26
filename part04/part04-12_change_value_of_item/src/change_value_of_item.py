# Write your solution here
index= int(input('Index:'))
list = [1,2,3,4,5]
while index != -1:
    value = int(input('New value'))
    list[index]=value
    print(list)
    index= int(input('Index:'))