#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    delete = []
    for x, y in a_dictionary.items():
        if y == value:
            delete.append(x)
    for x in delete:
        a_dictionary.pop(x)
    return a_dictionary
