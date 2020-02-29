import sys

sys.stdin = open('../../미해결/BOJ/input.txt')


def go(n, tmp):
    global min_ans
    if n >= 13:
        if tmp < min_ans:
            min_ans = tmp
        return

    go(n + 1, tmp + d * arr[n])
    go(n + 1, tmp + m1)
    go(n + 3, tmp + m3)


T = int(input())

for t in range(T):
    d, m1, m3, y = map(int, input().split())
    arr = [0] + list(map(int, input().split()))

    min_ans = y
    go(1, 0)

    print('#{} {}'.format(t + 1, min_ans))
