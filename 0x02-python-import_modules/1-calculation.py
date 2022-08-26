#!/usr/bin/python3
from calculator_1 import sub, mul, div, add


def main():
    """Main function
    a: first arg
    b: second arg
    """

    a = 10
    b = 5

    sum = add(a, b)
    diff = sub(a, b)
    product = mul(a, b)
    quotient = div(a, b)

    print("{} + {} = {}".format(a, b, sum))
    print("{} - {} = {}".format(a, b, diff))
    print("{} * {} = {}".format(a, b, product))
    print("{} / {} = {}".format(a, b, quotient))


if __name__ == '__main__':
    main()
