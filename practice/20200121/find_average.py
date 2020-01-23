T = int(input())
add = 0

for t in range(T):
    num = map(int, input().split(' '))
    for i in num:
        add += i
    print('#{} {}'.format(t+1, round(add/10)))
    add = 0