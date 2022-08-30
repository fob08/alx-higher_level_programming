#!usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv
if __name__ == "__main__"
argv
operator = argv[2]
operation = {"+": add, "-": sub, "*": mul, "/": div}
if len(user_input) != 4:
    print("Usage: {} <a> <operator> <b>".format(argv[0]))
    exit(1)
else:
    if operator not in operation:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        print("{} {} {} = {}".format(int(argv[1]), operator, int(argv[3]), operation[operator](int(argv[1]),int(argv[3]))))

