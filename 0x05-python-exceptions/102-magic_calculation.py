#!/usr/bin/python3
# using def magic_calculation(a, b) prototype

def magic_calculation(a, b):
    c = 0
    for idx in range(1, 3):
        try:
            if idx > a:
                raise Exception("Too far")
            c += a ** b / idx
        except Exception:
            c = b + a
            break
    return (c)
