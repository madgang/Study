module CalcMultiply
  def multiply()
    return @value1 * @value2
  end
end

module CalcDivide
  def divide()
    return @value1 / @value2
  end
end

class Calc
  include CalcMultiply, CalcDivide

  def initialize(value1, value2)
    if value1.is_a?(Integer)
      @value1 = value1
    end
    if value2.is_a?(Integer)
      @value2 = value2
    end
  end

  def add()
    return @value1 + @value2
  end

  def setValue(value)
    if value.is_a?(Integer)
      @value1 = value
    end
  end
  def getValue1()
    return @value1
  end
end

c = Calc.new(100,10)
p c.getValue1()
p c.multiply()
p c.divide()
p c.add()
