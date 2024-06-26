# Write your solution here
def spruce(base):
    print('a spruce!')
    for i in range (1, base+1):
        print(f'{(base-i)*" "}{(i*2-1)*"*"}{(base-i)*" "}')
    print(f'{(base-1)*" "}*{(base-1)*" "}')

# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(9)