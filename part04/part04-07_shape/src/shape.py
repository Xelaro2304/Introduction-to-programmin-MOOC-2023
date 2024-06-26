# Copy here code of line function from previous exercise and use it in your solution
def line(length, character):
    if character == '':
        print(length*'*')
    else:
        print(length*character[0])

def shape(width, triangle, height, square):
    for i in range (0, width):
        line(width**0+i, triangle)
    while height > 0:
        line(width, square)
        height -= 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")