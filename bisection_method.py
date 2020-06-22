class BisectionMethod():
    pi = 3.14159265359
    e = 2.71828182845

    def __init__(self, function, x, interval, precision):
        self.function = function
        self.x = x
        self.interval = interval
        self.precision = precision
        print(function(x))

    def graphic(self, interval):
        pass

def soma(x):
    return x[0] + x[1]

def subtraction(x):
    return x[0] - x[1]

sum = Root(soma, [1,2], 2, 3)
sub = Root(subtraction, [10, 4], 2, 4)