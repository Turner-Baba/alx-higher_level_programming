#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return o
    f = 0
    d = 0
    for num in my_list:
        f += num[0] * num[1]
        d += num[1]
    return (f / d )
