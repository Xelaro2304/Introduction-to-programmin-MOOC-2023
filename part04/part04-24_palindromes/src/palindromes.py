# Write your solution here
def palindromes (word):
    list1 = []
    list2 = []
    for j in word:
        list1.append(j)
    for k in range (-1,-len(word)-1,-1):
        list2.append(word[k])
    return list1 == list2            

def ask ():
    while True:
        word = input('Please type in a palindrome: ')
        if palindromes(word) == True:
            return print(f'{word} is a palindrome!')
        else:
            print("that wasn't a palindrome")
             
# Note, that at this time the main program should not be written inside
ask()
# block!
