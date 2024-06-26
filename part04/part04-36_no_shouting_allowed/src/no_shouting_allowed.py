# Write your solution here
def isupper(word):
    return word == word.upper()



def no_shouting(test):
    allowed_list=[]
    for i in test:
        scream = isupper(i)
        if scream == False:
            allowed_list.append(i)
    return allowed_list