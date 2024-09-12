#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div
ac = len(sys.argv) - 1
if ac != 3:
    sys.stderr.write("Usage: ./100-my_calculator.py <a> <operator> <b>")
    sys.exit(1)

a = int(sys.argv[1])
operator = sys.argv[2]
b = int(sys.argv[3])
if __name__ == "__main__":
    if operator == '+':
        print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
    elif operator == '-':
        print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
    elif operator == '*':
        print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
    elif operator == '/':
        print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
    else:
        sys.stderr.write("Unknown operator. Available\
                operators: +, -, *, and /")
        sys.exit(1)
