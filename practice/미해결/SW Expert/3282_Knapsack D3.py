import sys

sys.stdin = open('input.txt', 'r')


def go(k, cur_v, cur_c):
    global ans
    if cur_v > K:
        return
    if cur_v == K:
        if ans < cur_c:
            ans = cur_c
        return

    if k == N:
        return

    go(k+1, cur_v + li[k][0], cur_c + li[k][1])
    go(k+1, cur_v, cur_c)


T = int(input())

for t in range(T):
    N, K = map(int, input().split())
    li = []
    for i in range(N):
        li.append(list(map(int, input().split())))

    ans = 0
    go(0, 0, 0)

    print('#{} {}'.format(t + 1, ans))
