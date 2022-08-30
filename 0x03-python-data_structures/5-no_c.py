#!/usr/bin/python3
def no_c(my_string):
    stringg = []
    for i in my_string:
        if (ord(i) != ord"(c")) & (ord(i) != ord("C")):
            stringg.append(i)
        else:
            pass
    return(stringg)
