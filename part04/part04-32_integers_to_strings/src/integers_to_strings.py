# Write your solution here
def formatted (list):
    new_list = []
    for i in list:
        new_list.append(str(f'{i:.2f}'))
    return new_list



if __name__ == "__main__":
    formatted ([1.23, 2.777979])
