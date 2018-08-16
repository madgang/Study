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
    def info(self):
        return "Calc : value1 = %d, value2 = %d" %(self.value1,self.value2)
class CalcMultiply(Calc):
    def multiply(self):
        result = self.value1 * self.value2
        Calc._history.append("multiply : %d * %d = %d" % (self.value1,self.value2,result))
        return result
    def info(self):
        return "CalcMultiply => %s" % super().info()
class CalcDivide(CalcMultiply):
    def divide(self):
        result = self.value1 / self.value2
        Calc._history.append("divide : %d / %d = %d" % (self.value1,self.value2,result))
        return result
    def info(self):
        return "CalcDivide %s" % super().info()

calc = CalcMultiply(10,10)
# print(calc.add())
# print(calc.subtract())
# print(calc.multiply())
print(calc.info())
calc1 = CalcDivide(20,10)
#print(calc1.divide())
print(calc1.info())
Calc.history()
