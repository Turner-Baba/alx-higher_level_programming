#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for nopi in matrix:
        for tatt in nopi:
            print("{:d}".format(tatt), end=" " if tatt != nopi[-1] else "")
        print()
