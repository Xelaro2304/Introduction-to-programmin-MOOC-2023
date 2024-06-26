# Write your solution here
def same_chars(word, a, b):
    if a >= len(word) or b >= len(word):
        return False
    if word[a] == word[b]:
        return True
    else:
        return False
# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("abc", 0, 3))