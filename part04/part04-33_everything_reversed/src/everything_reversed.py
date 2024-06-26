# Write your solution here
def everything_reversed(a):
    list1 = []
    for i in a:
        list1.append(i)
    list1.reverse()
    for i in list1:
        j = list1.index(i)
        reverse = i[::-1]
        list1.pop(j)
        list1.insert(j, reverse)
    return list1


