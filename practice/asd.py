def go(num, cnt):
    if num == 0:
        return
    p = check(num)
    if p[0]:
        global ans
        cur = p[1] + cnt + 1
        if ans == -1 or ans > cur:
            ans = cur
        return
    for x, y in d:
        if x != 0 and x != 1:
            if num % x == 0:
                go(num // x, cnt + y + 1)
    return


def check(num):
    l = 0
    while num > 0:
        if not broken[num % 10]:
            return False, 0
        l += 1
        num //= 10
    return True, l


for t in range(int(input())):
    broken = list(map(int, input().split()))
    dap = int(input())
    d = []
    for i in range(2, int(dap ** (1 / 2)) + 1):
        if dap % i == 0:
            a = check(i)
            if a[0]:
                d.append((i, a[1]))
    ans = -1
    go(dap, 0)
    print('#{} {}'.format(t + 1, ans))