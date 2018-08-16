class C
  def initialize(v)
    @value = v
  end

  def show()
    p @value
  end
  def setValue(v)
    @value = v
  end
  def getValue()
    return @value
  end
end
c = C.new(10)
p c.getValue
c.setValue(20)
p c.getValue()
c.show();
