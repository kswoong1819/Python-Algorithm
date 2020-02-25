import sys

sys.stdin = open('../../2020_02/20200225/SW Expert/input.txt', 'r')


def go(k, n, start):
    global ans
    if k == n:
        if sum(V) == K:
            tmp = sum(C)
            if ans < tmp:
                ans = tmp
    for i in range(start, N):
        if check[i]:
            continue
        check[i] = True
        V.append(vi_li[i])
        C.append(ci_li[i])
        go(k + 1, n + 1, i + 1)
        V.pop()
        C.pop()
        check[i] = False


T = int(input())

for t in range(T):
    N, K = map(int, input().split())
    vi_li = []
    ci_li = []
    for i in range(N):
        vi, ci = map(int, input().split())
        vi_li.append(vi)
        ci_li.append(ci)

    ans = 0
    V = []
    C = []
    check = [False] * N
    go(0, 0, 0)

    print('#{} {}'.format(t + 1, ans))
