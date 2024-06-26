# write your solution here

def largest():
    with open("numbers.txt") as new_file:
        greatest = -1000000000000000000000000000000000
        for line in new_file:
            number = int(line)
            if greatest < number:
                greatest = number
        return greatest

print(largest())
