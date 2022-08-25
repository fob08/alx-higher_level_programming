#!/usr/bin/python3
argument = input("write your input")
arg_list = argument.split(" ")
for x in arg_list:
    print("{}: {}").format(((x.index) + 1), x)
