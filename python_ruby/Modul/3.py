import auth
login_id = input('아이디를 입력해주세요')
if auth.login(login_id):
    print('Hello '+login_id)
else:
    print('Who are you?')
