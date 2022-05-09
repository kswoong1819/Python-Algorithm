T = int(input())

for t in range(T):
    W, H, N = map(int, input().split())
    x, y = map(int, input().split())

    cnt = 0
    for i in range(N - 1):
        nx, ny = map(int, input().split())
        # if x == nx:
        #     cnt += abs(y - ny)
        # elif y == ny:
        #     cnt += abs(x - nx)
        if (x < nx and y > ny) or (x > nx and y < ny):
            cnt += abs(x - nx) + abs(y - ny)
        else:
            cnt += max(abs(x - nx), abs(y - ny))

        x, y = nx, ny

    print('#{} {}'.format(t+1, cnt))
