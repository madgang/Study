class Calc
  attr_reader :value1, :value2
  attr_writer :value1
  @@_history = []
  def initialize(value1,value2)
    @value1 = value1
    @value2 = value2
  end

  def add()
    result = @value1 + @value2
    @@_history.push("add : #{@value1} + #{@value2} = #{result}")
    return result
  end

  def subtract()
    result = @value1 - @value2
    @@_history.push("subtract : #{@value1} - #{@value2} = #{result}")
    return result
  end

  def setValue1(value1)
    if value1.is_a?(Integer)
      @value1 = value1
    end
  end

  def getValue1()
    return @value1
  end

  def Calc.history()
    for item in @@_history
      p item
    end

  end
end

class CalcMultiply < Calc
  def multiply()
    result = @value1 * @value2
    @@_history.push("multiply : #{@value1} * #{@value2} = #{result}")
    return result
  end
end

class CalcDivide < CalcMultiply
  def divide()
    result = @value1 / @value2
    @@_history.push("divide : #{@value1} / #{@value2} = #{result}")
    return result
  end
end

calc = CalcMultiply.new(10,10)
p calc.add()
p calc.multiply()

calc1 = CalcDivide.new(20,20)
p calc1.add()
p calc1.multiply()
p calc1.divide()
calc1.setValue1(40)
p calc1.divide()
p calc1.getValue1()
Calc.history()
