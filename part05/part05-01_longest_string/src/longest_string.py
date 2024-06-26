# Write your solution here
def longest(strings: list):
    longest = ''
    for string in strings:
        if len(longest) < len(string):
            longest = string
    return longest

if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))