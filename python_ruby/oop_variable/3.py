class Calc(object):
    def __init__(self,v1,v2):
        if isinstance(v1, int):
            self.v1 = v1
        if isinstance(v2, int):
            self.v2 = v2
    def add(self):
        return self.v1 + self.v2

    def subtract(self):
        return self.v1 - self.v2

    def setV1(self, v1):
        if isinstance(v1, int):
            self.v1 = v
    def getV1(self):
        return self.v1

c = Calc(10,10)
print(c.add())
print(c.subtract())

c.setV1('one')
c.v2 = 30
print(c.add())
print(c.subtract())
