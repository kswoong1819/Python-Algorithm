import sys

sys.stdin = open('../../미해결/SW Expert/input.txt', 'r')


def change_cnt():
    global ans
    for i in range(N - 2):
        for j in range(i + 1, N - 1):
            cnt = N * M - color_cnt[0][i]
            cnt -= color_cnt[1][j] - color_cnt[1][i]
            cnt -= color_cnt[2][N - 1] - color_cnt[2][j]
            if ans > cnt:
                ans = cnt


T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    flag_list = [list(input()) for _ in range(N)]
    color_cnt = [[flag_list[0].count('W')], [flag_list[0].count('B')], [flag_list[0].count('R')]]

    for i in range(1, N):
        color_cnt[0].append(flag_list[i].count('W') + color_cnt[0][i - 1])
        color_cnt[1].append(flag_list[i].count('B') + color_cnt[1][i - 1])
        color_cnt[2].append(flag_list[i].count('R') + color_cnt[2][i - 1])

    ans = N * M
    change_cnt()
    print('#{} {}'.format(t + 1, ans))
