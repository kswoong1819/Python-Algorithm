N = int(input())
start = 1
while 1:
    tmp = N * start
    if tmp > 100:
        break
    print(tmp, end=' ')
    start += 1
    if tmp % 10 == 0:
        break