# Write your solution here
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
            
                

def add_number(sudoku: list, row_no: int, column_no: int, number:int):
    sudoku[row_no][column_no] = number

