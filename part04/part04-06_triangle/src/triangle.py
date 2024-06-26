# Copy here code of line function from previous exercise
def line(length, character):
    if character == '':
        print(length*'*')
    else:
        print(length*character[0])


def triangle(size):
    # You should call function line here with proper parameters
    for i in range (0, size):
        line(size**0+i, "#")

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
