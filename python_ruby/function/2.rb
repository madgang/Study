def f5 a1
  return a1
end

def f6
  a = 1
  b = 4
  a + b
  c = 8
end

puts(f5 'f5ddd')
puts(f6)

puts('아이디 입력')
input_id = gets.chomp()

def login(_id)
  members = ['gang','gang0915','gang0915@gmail.com']
  return members.include?(_id)
end

if login(input_id)
  puts('Hello~ '+input_id)
else
  puts('Who are you?')
end
