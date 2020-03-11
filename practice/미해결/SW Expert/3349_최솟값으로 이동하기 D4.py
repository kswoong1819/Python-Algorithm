import sys
sys.stdin = open('../../2020_03/20200310/input.txt')

T = int(input())

for t in range(T):
    W, H, N = map(int, input().split())
    road = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0
    for i in range(N - 1):
        a = road[i]
        b = road[i + 1]
        while a != b:
            cnt += 1
            if a[0] < b[0] and a[1] < b[1]:
                a[0] += 1
                a[1] += 1
            if a[0] < b[0] and a[1] == b[1]:
                a[0] += 1
            if a[0] < b[0] and a[1] > b[1]:
                a[0] += 1
            if a[0] > b[0] and a[1] > b[1]:
                a[0] -= 1
                a[1] -= 1
            if a[0] > b[0] and a[1] == b[1]:
                a[0] -= 1
            if a[0] > b[0] and a[1] < b[1]:
                a[0] -= 1
            if a[0] == b[0] and a[1] > b[1]:
                a[1] -= 1
            if a[0] == b[0] and a[1] < b[1]:
                a[1] += 1

    print('#{} {}'.format(t+1, cnt))
