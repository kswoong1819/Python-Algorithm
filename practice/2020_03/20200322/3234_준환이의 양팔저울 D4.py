import sys

sys.stdin = open('input.txt')


def fact(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result


def go(k, left, right, total):
    global cnt
    if k == N:
        if left >= right:
            cnt += 1
        return
    if left >= total - left:
        tmp = 2 ** (N - k) * fact(N - k)
        cnt += tmp
        return
    for i in range(N):
        if used[i]:
            continue
        used[i] = 1
        go(k + 1, left + weight[i], right, total)
        used[i] = 0
        if left >= weight[i] + right:
            used[i] = 1
            go(k + 1, left, right + weight[i], total)
            used[i] = 0


T = int(input())

for t in range(T):
    N = int(input())
    weight = list(map(int, input().split()))

    cnt = 0
    used = [0] * N
    go(0, 0, 0, sum(weight))

    print('#{} {}'.format(t + 1, cnt))
