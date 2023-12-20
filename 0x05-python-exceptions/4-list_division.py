#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    qlist = []
    for idx in range(list_length):
        try:
            qt = my_list_1[idx] / my_list_2[idx]
        except TypeError:
            print("wrong type")
            qt = 0
        except ZeroDivisionError:
            print("division by 0")
            qt = 0
        except IndexError:
            print("out of range")
            qt = 0
        finally:
            qlist.append(qt)
    return (qlist)
