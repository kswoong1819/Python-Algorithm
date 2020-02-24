num = int(input())

while 1:
    result = 0
    while 1:
        result += num % 10
        num //= 10
        if num == 0:
            break
    print(result)
    if result >= 10:
        num = result
    else:
        break