#!usr/bin/python3
if __name__ == "__main__"
import calculator_1
user_input = input()
input_list = []
operator = [+, -, *, /]
input_list = input_list.append(user_input.split(" "))
if len(input_list) != 3:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
else:
    if input_list[1] == operator[0]:
        result = calculator_1.add(int(input_list[0]), int(input_list[2]))
        print(result)
        return(0)
    elif input_list[1] == operator[1]:
        result = calculator_1.sub(int(input_list[0]), int(input_list[2]))
    elif input_list[1] == operator[2]:
        result = calculator_1.mul(int(input_list[0]), int(input_list[2]))
    elif input_list[1] == operator[3]:
        result = calculator_1.div(int(input_list[0]), int(input_list[2]))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        return(1)

