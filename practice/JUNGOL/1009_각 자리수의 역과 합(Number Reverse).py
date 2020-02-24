while 1:
    num = int(input())
    if num == 0:
        break
    add = 0
    result = 0
    while 1:
        tmp = num % 10
        result += tmp
        add += tmp
        num //= 10
        if num > 0:
            result *= 10
        else:
            break
    print('{} {}'.format(result, add))