#!/usr/bin/python3

def square_matrix_map(matrix=[]):
    return list(map(lambda i: list(map(lambda d: d**2, i)), matrix))
