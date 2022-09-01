#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if a_dictionary:
        dic2 = {key:value}
        return(a_dictionary.update(dic2))
    else:
        return None
