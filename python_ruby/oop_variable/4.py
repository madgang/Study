class C(object):
    def __init__(self, v):
        self.__value = v
    def show(self):
        print(self.__value)

c = C(10)
#print(c.__value)
c.show()
