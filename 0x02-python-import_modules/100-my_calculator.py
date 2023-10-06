#!/usr/bin/python3

if __name__ == "__main__":
    """Handle basic arithmetic operations."""
    from calculator_1 import add, sub, mul, div
    from sys import argv

    if len(argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    operators = ["+", "-", "*", "/"]
    if argv[2] not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        a = int(argv[1])
        b = int(argv[3])
        if argv[2] == "+":
            print('{:d} + {:d} = {:d}'.format(a, b, add(a, b)))
        elif argv[2] == "-":
            print('{:d} - {:d} = {:d}'.format(a, b, sub(a, b)))
        elif argv[2] == "*":
            print('{:d} * {:d} = {:d}'.format(a, b, mul(a, b)))
        else:
            print('{:d} / {:d} = {:d}'.format(a, b, div(a, b))) 
            
