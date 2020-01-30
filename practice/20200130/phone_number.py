num = input()

while len(num) != 11:
    print('핸드폰번호를 입력하세요')
    num = input()
print('*'*7+num[-4:])