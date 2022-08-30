#!/usr/bin/python3
import hidden_4


def main():
    """a program that prints all the names
    defined by the compiled module hidden_4.pyc
    """

    hidden = (dir(hidden_4))
    for word in hidden:
        if word[0] not in '__':
            print(word)


if __name__ == '__main__':
    main()
