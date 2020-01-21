T = int(input())
result = 0

for t in range(T):
    num = map(int, input().split(' '))
    for j in num:
        if j % 2 != 0:
            result += j
    print('#{} {}'.format(t+1, result))
    result = 0