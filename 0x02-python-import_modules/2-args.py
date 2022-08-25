#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    for x in argv:
        print("{}: {}").format(((argv.index) + 1), x)
