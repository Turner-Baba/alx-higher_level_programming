#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    return [list(map((lambda tur: tur**2), r)) for r in matrix]
