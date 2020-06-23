import matplotlib.pyplot as plt 
import numpy as np

class BisectionMethod():
    def __init__(self, f, a, precision, result = []):
        self.f = f
        self.a = a
        self.precision = precision
        self.result = result

    def calculation(self):
        while True:
            p = (self.a[0] + self.a[1]) / 2
            self.result.append([p, self.f(p)])

            if abs(self.f(p)) <= self.precision:
                return self.result[-1][0]
                break

            else:
                if self.f(p)*self.f(self.a[0]) < 0:
                    self.a[1] = p
                else:
                    self.a[0] = p

    def outcome(self):
        return self.result

    def graphic(self):
        x = np.arange(self.a[0], self.a[1], 1)
        plt.axis([self.a[0], self.a[1], self.f(self.a[0]), self.f(self.a[1])])
        plt.grid()
        plt.plot(x, self.f(x))
        plt.show()

def function(x): 
    return x**2 - 25*x + 100

test = BisectionMethod(function, [0,11], 0.01)
test.graphic()
print(test.calculation())
print(test.outcome())
