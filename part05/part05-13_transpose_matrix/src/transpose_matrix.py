# Write your solution here
def transpose(matrix: list):
    trans_matrix=[]
    for r in matrix:
        trans_matrix.append(r[:])
    for i in range (len(trans_matrix)):
        for j in range(len(trans_matrix)):
            matrix[j][i] = trans_matrix[i][j]
