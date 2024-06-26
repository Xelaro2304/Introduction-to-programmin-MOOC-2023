# Write your solution here
def mean (value):
    sum = 0
    for i in value:
        sum += i
    return sum/len(value)
# You can test your function by calling it within the following block
if __name__ == "__main__":
    my_list = [3, 6, -4]
    result = mean(my_list)
    print(result)