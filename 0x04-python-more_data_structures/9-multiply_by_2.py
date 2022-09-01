#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if a_dictionary is not None:
        new_dict = {}
        temp_dict = {}
        for key, value in a_dictionary.items():
            valuess = value * 2
            temp_dict = {key, valuess}
            new_dict.update(temp_dict)
        return(new_dict)
    return None
