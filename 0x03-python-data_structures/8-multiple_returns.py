#!/usr/bin/python3

def multiple_returns(sentence):
    abc = ()
    if len(sentence) == 0:
        abc = 0, "None"
    else:
        abc = len(sentence), sentence[0]
        return abc
