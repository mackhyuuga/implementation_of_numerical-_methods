import matplotlib.pyplot as plt 
import numpy as np
import sqlite3

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

    def record(self):
        banco = sqlite3.connect('bisection_method.db')
        cursor = banco.cursor()
        cursor.execute("CREATE TABLE result (x REAL, 'f(x)' REAL)")
        for i in self.outcome:
            cursor.execute(f"INSERT INTO result VALUES({i[1]}, {i[2]})")
        banco.commit()

    def graphic(self):
        x = np.arange(self.a[0], self.a[1], 1)
        plt.axis([self.a[0], self.a[1], self.f(self.a[0]), self.f(self.a[1])])
        plt.grid()
        plt.plot(x, self.f(x))
        plt.show()

def function(x): 
    return x**2 - 25*x + 100

test = BisectionMethod(function, [0,11], 0.01)
print(test.calculation())
print(test.result())
