import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(T):
    num = float(input())
    result = ''
    cnt = 0
    while cnt < 14:
        num *= 2
        if num == 1:
            result += '1'
            break
        elif num > 1:
            result += '1'
            num -= 1
        else:
            result += '0'
        cnt += 1

    if cnt == 14:
        result = 'overflow'

    print('#{} {}'.format(t+1, result))
