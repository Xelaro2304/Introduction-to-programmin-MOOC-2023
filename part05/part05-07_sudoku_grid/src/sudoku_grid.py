# Write your solution here
def row_correct(sudoku: list):
    numbers = []
    for row in sudoku:
        for number in row:
            if number > 0 and number in numbers:
                return False
            numbers.append(number)
        numbers = []
    return True


def column_correct(sudoku: list):
    check_column=[]
    for column in range (len(sudoku)):
        for row in sudoku:
            number = row[column]
            if number > 0 and number in check_column:
                return False
            check_column.append(number)
        check_column = []
    return True


def block_correct(sudoku: list):
    check_block = []
    side = len(sudoku)
    for column in range (0, side, 3):
        for row in range(0, side, 3):
            for row_limit in range (0, 3):
                for col_limit in range (0, 3):
                    number = sudoku[row+row_limit][column+col_limit]
                    if number > 0 and number in check_block:
                        return False
                    check_block.append(number)
            check_block = []
    return True      


def sudoku_grid_correct(sudoku: list):
    check_row = row_correct(sudoku)
    check_column = column_correct(sudoku)
    check_block = block_correct(sudoku)
    if check_block == check_column == check_row == True:
        return True
    else:
        return False
