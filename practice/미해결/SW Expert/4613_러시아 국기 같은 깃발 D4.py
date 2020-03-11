import sys

sys.stdin = open('../../2020_03/20200311/input.txt', 'r')


def change_cnt(W, B):
    global ans
    if B < W:
        return
    cnt = 0
    for i in range(1, W):
        cnt += color_cnt[i][1] + color_cnt[i][2]
    for i in range(W, B+1):
        cnt += color_cnt[i][0] + color_cnt[i][1]
    for i in range(B+1, N-1):
        cnt += color_cnt[i][0] + color_cnt[i][2]
    if ans > cnt:
        ans = cnt
    change_cnt(W + 1, B)
    change_cnt(W, B - 1)


T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    flag_list = [list(input()) for _ in range(N)]
    color_cnt = []

    for i in range(N):
        count_W = flag_list[i].count('W')
        count_R = flag_list[i].count('R')
        count_B = flag_list[i].count('B')
        color_cnt.append([count_W, count_R, count_B])

    init = 0
    init += color_cnt[0][1] + color_cnt[0][2]
    init += color_cnt[N - 1][0] + color_cnt[N - 1][2]

    ans = 987654321
    change_cnt(1, N - 2)
    print('#{} {}'.format(t + 1, ans + init))
