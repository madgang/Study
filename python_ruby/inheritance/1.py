class Class1(object):
    def method1(self):
        return 'm1'

class Class2(object):
    def method1(self):
        return 'm1-1'

    def method2(self):
        return 'm2'
class Class3(Class1):
    def method2(self):
        return 'M2'

c1 = Class1()
print(c1, c1.method1())

c2 = Class2()
print(c2, c2.method1())

c3 = Class3()
print(c3, c3.method1())
