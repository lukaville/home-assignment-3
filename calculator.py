# coding: utf-8

from __future__ import division
from decimal import Decimal


operators = {
    "+": {"function": lambda x, y: x + y, "arg_number": 2},
    "-": {"function": lambda x, y: x - y, "arg_number": 2},
    "*": {"function": lambda x, y: x * y, "arg_number": 2},
    "/": {"function": lambda x, y: x / y, "arg_number": 2},
    "%": {"function": lambda x, y: x % y, "arg_number": 2}
}


def calculate(operator_name, *args):
    if operator_name not in operators:
        raise ValueError("Operator not supported")

    operator = operators[operator_name]
    if len(args) != operator["arg_number"]:
        raise ValueError("Argument count mismatch")

    args = map(lambda x: Decimal(x), args)

    return operator["function"](*args)
