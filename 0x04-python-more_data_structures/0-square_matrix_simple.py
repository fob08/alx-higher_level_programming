#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    mat = []
    new_matrix = []
    if matrix:
        for i in matrix:
            for j in i:
                mat.append(j^2)
            new_marrix.append(mat)
        return new_matrix
