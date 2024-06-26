# Write your solution here
def all_the_longest(list):
    k = 0
    word = []
    for i in list:
        if len(i) > k:
            k = len(i)
            word.clear ()
            word.append(i)
        elif len(i) == k:
            word.append(i)
    return word