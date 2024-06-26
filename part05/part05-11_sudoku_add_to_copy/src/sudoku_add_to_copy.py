# Write your solution here
def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    sudoku_copy = [[]for i in range(9)]
    for i in range(9):
        sudoku_copy[i] = sudoku[i][:]
    sudoku_copy[row_no][column_no] = number
    return sudoku_copy



def print_sudoku(sudoku: list):
    side = len(sudoku)
    for row in range (0, side):
        if row %3 == 0 and row !=0:
            print('')
        for column in range(0, side):
            number = sudoku[row][column]
            if column%3 == 0 and column != 0:
                print(' ', end='')
            if number == 0:
                print(f"_ ", end="")
            elif number != 0:
                print(f"{number} ", end='')
        print()

