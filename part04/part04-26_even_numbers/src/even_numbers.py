# Write your solution here
def even_numbers(list):
    evenlist = []
    for i in list:
        if i%2 == 0:
            evenlist.append(i)
    return evenlist


if __name__ == "__main__":
    even_numbers([1,1])