class C:
    def __init__(self, v):
        self.value = v

    def show(self):
        print(self.value);
    def setValue(self, v):
        self.value = v
    def getValue(self):
        return self.value


c = C(10)
print(c.getValue())
c.setValue(2)
print(c.getValue())
c.show()
