class Calc
  attr_reader :v1,:v2
  attr_writer :v1
  def initialize(v1,v2)
    @v1 = v1
    @v2 = v2
  end
  def add()
    return @v1+ @v2
  end

  def subtract()
    return @v1 - @v2
  end
  def setV1(v)
    if v.is_a?(Integer)
      @v1 = v
    end
   end
  def getV1()
    return @v1
  end
end

c = Calc.new(10,10)
p c.add()
p c.subtract()
c.setV1('one')
c.v1 = 20
p c.add()
p c.getV1()
