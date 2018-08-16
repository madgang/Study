require_relative 'Auth'
puts('아이디')
login_id = gets.chomp()
if(Auth.login(login_id))
  puts('Hello '+login_id)
else
  puts('Who are you?')
end
