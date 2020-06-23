from functools import reduce

def sum(x):
    return reduce(lambda x1, x2: x1 + x2, x)

def multiplication(x):
    return reduce(lambda x1, x2: x1 * x2, x)

def division(x):
    try:
        fractional = x[0] / x[1]
        integer = x[0] // x[1]
        rest = x[0] % x[1]
        return (fractional, integer, rest)
    except ZeroDivisionError:
        print("it is not possible to divide by zero")
        return None

