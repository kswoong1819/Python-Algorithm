import sys

sys.stdin = open('input.txt')


def go(k, L, T):
    global max_ans
    if L < 0:
        return
    if max_ans < T:
        max_ans = T
    if k == N:
        return
    go(k + 1, L - cal_list[k][1], T + cal_list[k][0])
    go(k + 1, L, T)


T = int(input())

for t in range(T):
    N, L = map(int, input().split())
    cal_list = []
    for i in range(N):
        cal_list.append(list(map(int, input().split())))
    max_ans = 0
    go(0, L, 0)
    print('#{} {}'.format(t+1, max_ans))
