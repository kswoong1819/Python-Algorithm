import sys

sys.stdin = open('input.txt')


def check(n):
    l = 0
    while n > 0:
        tmp = n % 10
        if tmp not in nums:
            return False, 0
        l += 1
        n //= 10
    return True, l


def go(num, cnt):
    global ans
    if num == 0:
        return
    n = check(num)
    if n[0]:
        tmp = n[1] + cnt + 1
        if ans == -1 or ans > tmp:
            ans = tmp
        return
    for x, y in d:
        if x != 0 and x != 1:
            if num % x == 0:
                go(num // x, cnt + y + 1)
    return


T = int(input())
res = []
for t in range(T):
    calcul = list(map(int, input().split()))
    X = int(input())
    nums = [i for i in range(10) if calcul[i]]

    d = []
    for i in range(2, int(X ** (1 / 2)) + 1):
        if X % i == 0:
            p = check(i)
            if p[0]:
                d.append((i, p[1]))

    ans = -1
    go(X, 0)
    res.append('#{} {}'.format(t + 1, ans))
print('\n'.join(res))
