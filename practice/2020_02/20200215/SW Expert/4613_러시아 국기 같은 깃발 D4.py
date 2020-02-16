import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(T):
    N , M = map(int, input().split())
    flag_list = [list(input()) for _ in range(N)]
    color_cnt = []
    result = 0

    for i in range(N):
        count_W = flag_list[i].count('W')
        count_R = flag_list[i].count('R')
        count_B = flag_list[i].count('B')
        color_cnt.append([count_W, count_R, count_B])


    result += color_cnt[0][1] + color_cnt[0][2]

    max = 0
    for i in range(N):
        if color_cnt[i][2] > max:

