login_id = input('아이디 입력')

def login(_id):
    members = ['gang','gang0915','gang0915@gmail.com']
    return members.count(_id) > 0
if login(login_id):
    print('Hello '+login_id)
else :
    print('Who are you?')
