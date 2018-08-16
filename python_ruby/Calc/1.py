class Calc(object):
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2

    def add(self):
        return self.v1 + self.v2

    def subtract(self):
        return self.v1 - self.v2

c1 = Calc(10,10)
print(c1.add())
print(c1.subtract())

c2 = Calc(20,30)
print(c2.add())
print(c2.subtract())
