al = ['A','B','C','D']
puts(al.length)
al.push('E')
puts(al)
al.delete_at(0)
print("\n")
print(al)

i = 0
while i < 10 do
  puts('puts(\'Hello world\''+(i * 9).to_s()+')')
  i = i + 1
end
puts('after while')
