# Write your solution here
def squared(word, length):
    wordword = word*length
    for i in range (0, length):
        print(wordword[length*i:length*(i+1)])
        wordword += word*length
if __name__ == "__main__":
    squared('ab', 3)