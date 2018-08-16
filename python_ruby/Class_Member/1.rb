require 'date'
d1 = Date.new(2001,1,1)
d2 = Date.new(2012,1,1)

p d1.year()
p d2.year()

p Date.today().wday()
class Cs
   def Cs.class_method()
    p "Class method"
   end
   def instance_method()
     p "instance_metho"
   end

end

i = Cs.new()
i.instance_method()
Cs.class_method()
#i.class_method()
#Cs.instance_method
