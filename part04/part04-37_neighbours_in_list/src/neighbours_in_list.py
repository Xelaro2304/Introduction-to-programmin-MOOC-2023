# Write your solution here
def longest_series_of_neighbours(list):
    count = 1
    longest = 0
    for i in range (0, len(list)-1):
        if list[i] == list[i+1]+1 or list[i] == list[i+1]-1:
            count += 1 
            if count > longest:
                longest = count
        else:
            count = 1
    return  longest

if __name__ == "__main__":
    my_list = [1, 2, 3, 5, 6, 7, 6, 5, 6, 7, 10, 11, 10]
    print(longest_series_of_neighbours(my_list))