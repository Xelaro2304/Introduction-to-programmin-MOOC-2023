# Write your solution here
def length_of_longest(list):
    k = 0
    for i in list:
        if len(i) > k:
            k = len(i)
    return k

if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]
    result = length_of_longest(my_list)
    print(result)