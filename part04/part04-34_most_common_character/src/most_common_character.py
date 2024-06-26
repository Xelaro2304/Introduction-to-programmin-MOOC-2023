# Write your solution here
def most_common_character (word):
    highest = 0
    for i in word:
        if word.count(i) > highest:
            highest = word.count(i)
            most = i
    return (most)

if __name__ == "__main__":
    most_common_character("abc")