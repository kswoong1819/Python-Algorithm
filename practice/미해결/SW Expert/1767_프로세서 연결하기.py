import sys
import copy

sys.stdin = open('../../2020_05/0507/input.txt')

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def go(board, cur, core_cnt):
    global ans, core
    if core <= core_cnt:
        ans[core_cnt].append(cur)
    for i in range(1, N - 1):
        for j in range(1, N - 1):
            if board[i][j] == 1:
                n_arr, cnt = connect(i, j, board)
                if cnt:
                    go(n_arr, cur + cnt, core_cnt + 1)
                else:
                    return


def connect(r, c, board):
    n_board = copy.deepcopy(board)
    for i in range(4):
        n_board[r][c] = 3
        nr = r
        nc = c
        cnt = 0
        while 1:
            nr += dr[i]
            nc += dc[i]
            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                return n_board, cnt
            if n_board[nr][nc] > 0:
                while nr != r or nc != c:
                    nr -= dr[i]
                    nc -= dc[i]
                    n_board[nr][nc] = 0
                break
            if n_board[nr][nc] == 0:
                n_board[nr][nc] = 2
                cnt += 1
    return 0, 0


T = int(input())

for t in range(T):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    ans = [[] for _ in range(12)]
    core = 0
    go(board, 0, 0)

    for i in range(11, -1, -1):
        if len(ans[i]):
            print(min(ans[i]))
            break
