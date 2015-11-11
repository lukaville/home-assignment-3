# coding: utf-8

operators = {
    "+": {"function": lambda x, y: x + y, "arg_number": 2},
    "-": {"function": lambda x, y: x - y, "arg_number": 2},
    "*": {"function": lambda x, y: x * y, "arg_number": 2},
    "/": {"function": lambda x, y: x / y, "arg_number": 2},
    "%": {"function": lambda x, y: x % y, "arg_number": 2}
}


def calculate(op, *args):
    if op not in operators:
        raise ValueError("Operator not supported")

    opeator = operators[op]
    if len(args) != opeator["arg_number"]:
        raise ValueError("Argument count mismatch")

    return opeator["function"](*args)
