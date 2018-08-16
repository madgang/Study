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

class CalcMultiply < Calc
  def multiply()
    return @v1 * @v2
  end
end

class CalcDivide < CalcMultiply
  def devide()
    return @v1 / @v2
  end
end

calc = CalcDivide.new(20,10)
p calc.add()
p calc.multiply()
p calc.devide()
calc.setV1(40)
p calc.add()
