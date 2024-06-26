# Write your solution here
def shortest(list):
    k = 500
    for i in list:
        if len(i) < k:
            k = len(i)
            word = i
    return word

