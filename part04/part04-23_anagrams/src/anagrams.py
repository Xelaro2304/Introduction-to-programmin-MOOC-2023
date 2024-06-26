# Write your solution here
def anagrams (word, drow):
    list1 = []
    list2 = []
    for j in word:
        list1.append(j)
    for k in drow:
        list2.append(k)
    for i in word:
        if i in list2:
            list1.remove(i)
            list2.remove(i)
    if list1 == list2:
        return True
    else:
        return False
    
if __name__ == "__main__":
    print(anagrams("house", "esuoh"))