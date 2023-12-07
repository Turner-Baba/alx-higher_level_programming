#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    sortedkeys = sorted(a_dictionary)
    for k in sortedkeys:
        print("{:s}: {}".format(k, a_dictionary[k]))
