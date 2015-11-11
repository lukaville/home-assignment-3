# coding: utf-8

from __future__ import print_function
from calculator import calculate


def main():
    try:
        opeator = str(raw_input("Enter operator name: "))
        arguments_string = str(raw_input("Enter arguments: "))
        arguments = map(lambda x: int(x), arguments_string.split())
        print(calculate(opeator, *arguments))
    except Exception as e:
        print("Sorry, error occurred: " + e.message)

if __name__ == "__main__":
    main()
