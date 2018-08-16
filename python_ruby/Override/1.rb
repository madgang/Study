class C1
  def m()
    return 'Parent'
  end
end

class C2 < C1
  def m()
    return super() + ' + Childe'
  end
end

o = C2.new()
p o.m()
