#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is not None:
        for i in a_dictionary:
            if i.value() > (i + 1).value():
                a = i.key()
            else:
                a = (i + 1).key()
        return  a
    else:
        None
