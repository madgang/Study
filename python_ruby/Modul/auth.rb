module Auth
  module_function()
  def login(_login)
    members = ['madgang','gang0915','gang0915@gmail.com']
    return members.include?(_login)
  end
end
