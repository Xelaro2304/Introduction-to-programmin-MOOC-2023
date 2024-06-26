# Write your solution here
def row_correct(sudoku: list, row_no: int):
    sudoku_check = sudoku[row_no]
    for i in range (1, 10):
        if sudoku_check.count(i) > 1:
            return False
    return True