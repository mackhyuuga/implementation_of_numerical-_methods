import matplotlib.pyplot as plt 
import numpy as np

class BisectionMethod():
    def __init__(self, f, a, precision, outcome = []):
        self.f = f
        self.a = a
        self.precision = precision
        self.outcome = outcome

    def calculation(self):
        n = 0
        while True:
            p = (self.a[0] + self.a[1]) / 2
            n += 1
            self.outcome.append([n, p, self.f(p)])

            if abs(self.f(p)) <= self.precision:
                return self.outcome[-1][1]
                break

            else:
                if self.f(p)*self.f(self.a[0]) < 0:
                    self.a[1] = p
                else:
                    self.a[0] = p

    def result(self):
        return self.outcome

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
print(test.result())
