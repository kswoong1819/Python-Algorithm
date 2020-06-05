import sys

sys.stdin = open('input.txt')
from collections import deque

dr = [0, -1, 0, 1, 0]
dc = [0, 0, 1, 0, -1]


def set_area(num, x, y, c, p):
    board[x][y].append([p, num])
    q = deque()
    q.append([x, y, c])
    while q:
        x, y, c = q.popleft()
        if c == 0:
            continue
        for i in range(1, 5):
            nr = x + dr[i]
            nc = y + dc[i]
            if 0 <= nr < 10 and 0 <= nc < 10:
                if [p, num] not in board[nr][nc]:
                    board[nr][nc].append([p, num])
                    q.append([nr, nc, c - 1])


def charge():
    A = [0, 0, 0, 0]
    B = [9, 9, 0, 0]
    if board[0][0]:
        board[0][0].sort()
        A[3] += board[0][0][-1][0]
        A[2] = board[0][0][-1][1]
    if board[9][9]:
        board[9][9].sort()
        B[3] += board[9][9][-1][0]
        B[2] = board[9][9][-1][1]
    for i in range(M):
        A[0] += move_A[i]
        A[1] += move_A[i]
        B[0] += move_B[i]
        B[1] += move_B[i]
        if board[A[0]][A[1]]:
            board[A[0]][A[1]].sort()
            A[2] = board[A[0]][A[1]][-1][-1]
        if board[B[0]][B[1]]:
            board[B[0]][B[1]].sort()
            B[2] = board[B[0]][B[1]][-1][-1]
        if A[2] != 0 and A[2] == B[2]:
            if len(board[A[0]][A[1]]) >= 2:
                A[3] += board[A[0]][A[1]][-1][0]
                B[3] += board[B[0]][B[1]][-1][0]




T = int(input())
for t in range(T):
    M, A = map(int, input().split())
    move_A = list(map(int, input().split()))
    move_B = list(map(int, input().split()))
    board = [[[] for _ in range(10)] for _ in range(10)]
    for a in range(A):
        Y, X, C, P = map(int, input().split())
        set_area(a + 1, X - 1, Y - 1, C, P)

    charge()
