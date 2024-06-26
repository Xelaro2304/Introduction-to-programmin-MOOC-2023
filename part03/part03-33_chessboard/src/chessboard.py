# Write your solution here
def chessboard(length):
    for i in range (0,length):
        if i%2 == 0:
            for j in range (0, length):
                if j%2 == 1:
                    print(0, end='')
                else: 
                    print(1, end='')
        else:
            for j in range (0, length):
                if j%2 == 1:
                    print(1, end='')
                else: 
                    print(0, end='')
        print('')
# Testing the function
if __name__ == "__main__":
    chessboard(50)
