# Write your solution here
def column_correct(sudoku: list, column_no: int):
    check_column=[]
    for row in sudoku:
        if row[column_no] > 0 and row[column_no] in check_column:
            return False
        check_column.append(row[column_no])
    return True
