#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return 'None'
    else:
        biggestint = my_list[0]
        for digit in my_list:
            if digit > biggestint:
                biggestint = digit
        return biggestint
