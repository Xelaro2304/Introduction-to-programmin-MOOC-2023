# Write your solution here
def distinct_numbers (a):
    
    for i in a:
        new_list = []
        for j in range (-1, -len(a)+a.index(i), -1):
            if i == a[j]:
                new_list.append(j)
        for k in sorted(new_list):
            a.pop(k)
    return sorted(a)
        


if __name__ == "__main__":
    my_list = [1,2]
    distinct_numbers(my_list)