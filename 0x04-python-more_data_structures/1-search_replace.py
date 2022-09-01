#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list:
        for i in my_list:
            if i != search:
                return i
            else:
                return replace
    return None
