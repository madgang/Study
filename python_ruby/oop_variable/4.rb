class C
  # attr_reader :value
  # attr_writer :value
  attr_accessor :value
  def initialize(v)
    @value = v
  end
  def show()
    return @value
  end
end

c = C.new(10)
p c.value
p c.show()
c.value = 20;
p c.value;
