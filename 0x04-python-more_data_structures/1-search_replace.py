#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list:
        for i in my_list:
            if i != search:
                pass
            else:
                my_list[i] = replace
        return my_list
    return None
