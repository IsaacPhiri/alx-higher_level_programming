#!/usr/bin/python3
import sys


def main():
    """main
    """

    n = len(sys.argv)
    sum = 0

    for i in range(1, n):
        sum += int(sys.argv[i])

    print("{}".format(sum))


if __name__ == '__main__':
    main()
