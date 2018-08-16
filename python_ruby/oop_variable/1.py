# class C:
#     def __init__(self, v):
#         self.value = v
#
#     def show(self):
#         print(self.value);
# c = C(10)
# print(c.value)
# c.value = 20
# print(c.value)
# c.show()

# class foo(object):
#     name = 'foo'
#     @staticmethod
#     def get_name_static():
#         print foo.name
#     @classmethod
#     def get_name_class(cls):
#         print cls.name
# class bar(foo):
#     name = 'bar'
#
# bar.get_name_static() #foo
# bar.get_name_class() #bar

class foo(object):
    @classmethod
    def set_name(cls,name):
        cls.name = name
class bar(foo):
    pass

print foo.set_name('foo')
print foo.name
print bar.name
print bar.set_name('bar')
print foo.name
print bar.name
