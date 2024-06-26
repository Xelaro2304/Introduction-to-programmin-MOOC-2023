# Write your solution here
def first_word(sen):
    return sen[0:sen.find(' ')]
def second_word(sen2):
    newsen = sen2[len(first_word(sen2))+1:]
    word2 = ''
    if ' ' not in newsen:
        for i in range (0, len(newsen)):
            word2 += newsen[i]
        return word2
    else:
        return newsen[0:newsen.find(' ')]
def last_word(sen3):
    word3 = ''
    j=0
    last=''
    while sen3[-1+j]!=' ':
       word3 += sen3[-1+j]
       j -= 1
    for i in range (-1, -len(word3)-1, -1):
       last += word3[i]
    return last
#def last_word(sentence):
    
# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))
    