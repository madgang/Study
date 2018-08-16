class Calc(object):
    _history = []
    def __init__(self,value1,value2):
        if isinstance(value1, int):
            self.value1 = value1
        if isinstance(value2, int):
            self.value2 = value2
    def add(self):
        result = self.value1 + self.value2
        Calc._history.append("add : %d + %d = %d" % (self.value1,self.value2,result))
        return result
    def subtract(self):
        result = self.value1 - self.value2
        Calc._history.append("subtract : %d - %d = %d" % (self.value1,self.value2,result))
        return result
    def setValue1(self,value1):
        if isinstance(value1,int):
            self.value1 = value1
    def gatValue1(self):
        return self.value1
    @classmethod
    def history(cls):
        for item in Calc._history:
            print(item)
class CalcMultiply(Calc):
    def multiply(self):
        result = self.value1 * self.value2
        Calc._history.append("multiply : %d * %d = %d" % (self.value1,self.value2,result))
        return result
class CalcDivide(CalcMultiply):
    def divide(self):
        result = self.value1 / self.value2
        Calc._history.append("divide : %d / %d = %d" % (self.value1,self.value2,result))
        return result

calc = CalcMultiply(10,10)
print(calc.add())
print(calc.subtract())
print(calc.multiply())
calc1 = CalcDivide(20,10)
print(calc1.divide())
Calc.history()
