T = int(input())

for t in range(T):
    D, H, M = map(int, input().split())

    day_1111 = 11 * 24 * 60 + 11 * 60 + 11

    total = D * 24 * 60 + H * 60 + M - day_1111

    if total < 0:
        print('#{} -1'.format(t+1))
    else:
        print('#{} {}'.format(t+1, total))
