import sys

sys.stdin = open('input.txt')


def go(n, s):
    global min_ans

    if n >= 13:
        if min_ans > s:
            min_ans = s
        return

    go(n + 1, s + d * month[n-1])
    go(n + 1, s + m1)
    go(n + 3, s + m3)


T = int(input())

for t in range(T):
    d, m1, m3, y = map(int, input().split())
    month = list(map(int, input().split()))

    min_ans = y
    go(1, 0)

    print('#{} {}'.format(t + 1, min_ans))
