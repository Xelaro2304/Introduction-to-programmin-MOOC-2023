# Copy here code of line function from previous exercise

def square(size, character1):
    # You should call function line here with proper parameters
    for i in range (size, 0, -1):
        line(size, character1)

def line(length, character):
    if character == '':
        print(length*'*')
    else:
        print(length*character[0])
# You can test your function by calling it within the following block
if __name__ == "__main__":
    square(5, "x")