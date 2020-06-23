def baskara(x):
    try:
        delta = x[1] ** 2 - 4 * x[0] * x[2]
        x1 = (-x[1] + (delta) ** 0.5) / (2 * x[0])
        x2 = (-x[1] - (delta) ** 0.5) / (2 * x[0])
        return (x1, x2)

    except IndexError:
        print('error in the input parameters')
        return None
