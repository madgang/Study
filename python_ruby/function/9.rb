arr = ['a','b','c',124]
#arr.each(){|i| puts i}

for value in arr
  puts(value.class)
end

arrs = [1,3,5,7,19,40]
arrs.delete_if() do
  |item|
  item > 1 && item < 7
end
puts arrs
