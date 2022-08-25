#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    user_input = argv
    user_input = user_input.split(",")
    if len(user_input) == 0:
        print(".")
    else:
        for x in user_input:
            print("{}: {}").format(((argv.index) + 1), x)
