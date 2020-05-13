import sys

sys.stdin = open('input.txt')
from collections import deque

dr = [-1, -2, -2, -1, 1, 2, 2, 1]
dc = [-2, -1, 1, 2, 2, 1, -1, -2]


# def bfs(st):
#     q = deque()
#     q.append(st)
#     while q:
#         r, c, cnt = q.popleft()
#         if r == nxt_r and c == nxt_c:
#             print(cnt)
#             return
#         for i in range(8):
#             nr = r + dr[i]
#             nc = c + dc[i]
#             if 0 <= nr < l and 0 <= nc < l and board[nr][nc] == 0:
#                 board[nr][nc] = 1
#                 q.append([nr, nc, cnt + 1])


def bfs_2(r, c):
    q_2 = deque()
    q_2.append([r, c])
    while q_2:
        r, c = q_2.popleft()
        if r == nxt_r and c == nxt_c:
            print(board_2[r][c]-1)
            return
        for i in range(8):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < l and 0 <= nc < l and board_2[nr][nc] == 0:
                board_2[nr][nc] = board_2[r][c] + 1
                q_2.append([nr, nc])



T = int(input())

for t in range(T):
    l = int(input())
    cur_r, cur_c = map(int, input().split())
    nxt_r, nxt_c = map(int, input().split())

    # board = [[0] * l for _ in range(l)]
    # board[cur_r][cur_c] = 1
    # bfs([cur_r, cur_c, 0])

    board_2 = [[0] * l for _ in range(l)]
    board_2[cur_r][cur_c] = 1
    bfs_2(cur_r, cur_c)