#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    newtuple = ()
    t_1 = tuple_a + (0, 0)
    t_2 = tuple_b + (0, 0)
    newtuple = t_1[0] + t_2[0], t_1[1] + t_2[1]
    return newtuple
