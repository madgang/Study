class C
  def initialize(v)
    @value = v
  end

  def show()
    p @value
  end
end
c = C.new(10)
# p c.value
# c.value = 20
c.show();
