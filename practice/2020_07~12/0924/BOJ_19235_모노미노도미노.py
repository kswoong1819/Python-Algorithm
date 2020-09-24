import sys

sys.stdin = open('input.txt')
from collections import deque

def delline(ch, n):
    if ch == "g":
        G_board[n] = [0] * 4
        for domi in G:
            i = 0
            while len(domi) != 0:
                if domi[i][0] == n:
                    domi.pop(i)
                    continue
                else:
                    len(domi) != 0
    print(G)

N = int(input())
G_board = [[0] * 4 for _ in range(6)]
B_board = [[0] * 6 for _ in range(4)]
G = []
B = []
for i in range(N):
    t, x, y = map(int, input().split())
    if t == 1:
        r, c = [0, y]
        while 1:
            r += 1
            if r > 5 or G_board[r][c] == 1:
                G_board[r - 1][c] = 1
                G.append([[r - 1, c]])
                if G_board[c].count(1) == 4:
                    print(True)
                break
        r, c = [x, 0]
        while 1:
            c += 1
            if c > 5 or B_board[r][c] == 1:
                B_board[r][c - 1] = 1
                B.append([[r, c-1]])
                break
    if t == 2:
        block = [[0, y], [0, y + 1]]
        cnt = 0
        while cnt >= 0:
            k = 0
            cnt += 1
            while k <= 1:
                r, c = block[k]
                r += cnt
                if r > 5 or G_board[r][c] == 1:
                    G_board[r - 1][y] = G_board[r - 1][y + 1] = 1
                    G.append([[r - 1, y], [r - 1, y + 1]])
                    cnt = -1
                    if G_board[y].count(1) == 4:
                        print(True)
                    break
                else:
                    k += 1
        r, c = [x, 1]
        while 1:
            c += 1
            if c > 5 or B_board[r][c] == 1:
                B_board[r][c - 2] = B_board[r][c - 1] = 1
                B.append([[r, c-2], [r, c-1]])
                break
    if t == 3:
        r, c = [1, y]
        while 1:
            r += 1
            if r > 5 or G_board[r][c] == 1:
                G_board[r - 2][c] = G_board[r - 1][c] = 1
                G.append([[r - 2, c], [r - 1, c]])
                if G_board[r-2].count(1) == 4:
                    delline("g", r-2)
                if G_board[r-1].count(1) == 4:
                    print(True)
                break
        block = [[x, 0], [x+1, 0]]
        cnt = 0
        while cnt >= 0:
            k = 0
            cnt += 1
            while k <= 1:
                r, c = block[k]
                c += cnt
                if c > 5 or B_board[r][c] == 1:
                    B_board[x][c-1] = B_board[x+1][c-1] = 1
                    B.append([[x, c-1], [x + 1, c + 1]])
                    cnt = -1
                    break
                else:
                    k += 1


for g in G_board:
    print(g)
for b in B_board:
    print(b)