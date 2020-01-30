'''
로그인 로직을 검증하는 함수 login 을 작성하세요.

login 함수는 username, password, password_confirmation을 인자로 받는다.
login 함수는 username과, password가 있는지 확인한다.
password가 8자리 이상인지 확인한다.
password와 password_confirmation이 일치하는지 확인한다.
'''

my_account = {
    'username': '홍길동',
    'password': '1q2w3e4r',
    'password_confirmation': '1q2w3e4r'
}

def login(username, password, password_confirmation):
    if len(password) < 8:
        return '비밀번호가 8자리가 아닙니다.'
    if password == password_confirmation:
        return '{}님 반갑습니다.'.format(username)
    return '비밀번호와 비밀번호확인이 일치하지 않습니다.'

print(login(**my_account))