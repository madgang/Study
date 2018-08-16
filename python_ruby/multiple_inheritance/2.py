class CalcMultiply():
    def multiply(self):
        return self.value1 * self.value2

class CalcDivide():
    def divide(self):
        return self.value1 / self.value2

class Calc(CalcMultiply, CalcDivide):
    def __init__(self, value1, value2):
        if isinstance(value1,int):
            self.value1 = value1
        if isinstance(value2,int):
            self.value2 = value2

    def add(self):
        return self.value1 + self.value2

    def subtract(self):
        return self.value1 - self.value2

    def setValue1(self, value1):
        if isinstance(value1,int):
            self.value1 = value1

    def getValue(self):
        return self.value1

c = Calc(100,10)
print(c.add())
print(c.multiply())
print(c.subtract())
print(c.divide())
