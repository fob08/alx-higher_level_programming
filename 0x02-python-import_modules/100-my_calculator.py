#!usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv
if __name__ == "__main__"
input_list = argv
operator = [+, -, *, /]
if len(user_input) != 4:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    exit(1)
else:
    if input_list[2] == operator[0]:
        result = add(int(input_list[1]), int(input_list[3]))
        print(result)
        exit(0)
    elif input_list[2] == operator[1]:
        result = sub(int(input_list[1]), int(input_list[3]))
        print(result)
        exit(0)
    elif input_list[2] == operator[2]:
        result = mul(int(input_list[1]), int(input_list[3]))
        print(result)
        exit(0)
    elif input_list[2] == operator[3]:
        result = div(int(input_list[1]), int(input_list[3]))
        print(result)
        exit(0)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

