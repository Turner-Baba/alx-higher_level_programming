#!/usr/bin/python3

def uniq_add(my_list=[]):
    uniqlist = set(my_list)
    add = 0
    for num in uniqlist:
        add += num
    return (add)
