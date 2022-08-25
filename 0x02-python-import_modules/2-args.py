#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    user_input = argv[1:]
    print("{:d} {:s}{:s}").format(len(user_input), "arguments" if len(user_input) != 1 else "argument", "." if len(user_input) == 0 else ":")
    for x in user_input:
        print("{:d}: {:s}").format(((x.index) + 1), x)
