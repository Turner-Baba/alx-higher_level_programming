#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    newlist = []
    for e in my_list:
        newlist.append(e)
    if idx < 0 or idx >= len(my_list):
        return newlist
    else:
        newlist[idx] = element
        return newlist
