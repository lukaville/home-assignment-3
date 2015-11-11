# coding: utf-8

from __future__ import print
from calculator import calculate


def main():
    try:
        print(calculate("+", 1, 2))
    except Exception as e:
        print("Sorry, error occurred: " + e.message)

if __name__ == "__main__":
    main()
