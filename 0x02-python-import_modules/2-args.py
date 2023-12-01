#!/usr/bin/python3
# python program that prints number of and lists of its arguments

if __name__ == "__main__":
    from sys import argv
    argc = len(argv) - 1
    if argc == 0:
        print("0 arguments.")
    elif argc == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(argc))
    for x in range(argc):
        print("{}: {}".format(x + 1, argv[x + 1]))
