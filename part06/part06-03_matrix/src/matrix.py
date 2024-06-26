# write your solution here
def matrix_reader():
    with open("matrix.txt") as new_file:
        matrix=[]
        for line in new_file:
            line = line.replace("\n", "")
            string_list = line.split(',')
            number_list = []
            for i in string_list:
                number_list.append(int(i))
            matrix.append(number_list)
        return matrix



def row_sums():
    matrix = matrix_reader()
    
    highest=[]
    for row in matrix:
        row_sum = 0
        for number in row:
            row_sum += number
        highest.append(row_sum)
    return(highest)
    


def matrix_max():
    matrix = matrix_reader()
    highest=0
    for row in matrix:
        for number in row:
            if number > highest:
                highest = number
    return(highest)



def matrix_sum():
    matrix = matrix_reader()
    total=0
    for row in matrix:
        for number in row:
            total += number
    return(total)