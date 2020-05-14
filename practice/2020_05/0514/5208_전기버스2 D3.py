import sys

sys.stdin = open('input.txt')


def go(st, ed, cnt):
    global ans
    if cnt > ans:
        return
    if st >= ed:
        ans = min(ans, cnt - 1)
        return
    for i in range(st + station[st], st, -1):
        go(i, ed, cnt + 1)


T = int(input())
for t in range(T):
    station = list(map(int, input().split()))

    ans = 999
    go(1, station[0], 0)

    print('#{} {}'.format(t + 1, ans))
