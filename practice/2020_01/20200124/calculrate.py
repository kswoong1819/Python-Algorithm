num1, num2 = map(int, input().split(' '))

if 1<=num1<=9 and 1<=num2<=9:
    print(num1 + num2)
    print(num1 - num2)
    print(num1 * num2)
    print(int(num1/num2))
else:
    print('1~9 까지 숫자를 입력해주세요.')