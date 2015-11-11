# coding: utf-8

functions = {
    "+": {"function": lambda x, y: x + y, "arg_number": 2},
    "-": {"function": lambda x, y: x - y, "arg_number": 2},
    "*": {"function": lambda x, y: x * y, "arg_number": 2},
    "/": {"function": lambda x, y: x / y, "arg_number": 2},
    "%": {"function": lambda x, y: x % y, "arg_number": 2}
}


def calculate(function, *args):
    if function not in functions:
        raise ValueError("Operator not supported")
    return functions[function]["function"](*args)
