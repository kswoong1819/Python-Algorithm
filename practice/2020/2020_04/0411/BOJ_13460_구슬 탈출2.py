import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def move(x, y, dr, dc):
    cnt = 0
    while board[x + dr][y + dc] != '#' and board[x][y] != 'O':
        x += dr
        y += dc
        cnt += 1
    return x, y, cnt


def bfs(st):
    q = deque()
    q.append(st)
    while q:
        rx, ry, bx, by, depth = q.popleft()
        visited[rx][ry][bx][by] = 1
        if depth > 10:
            break
        for i in range(4):
            nrx, nry, rcnt = move(rx, ry, dr[i], dc[i])
            nbx, nby, bcnt = move(bx, by, dr[i], dc[i])
            if board[nbx][nby] == 'O':
                continue
            if board[nrx][nry] == 'O':
                print(depth)
                return
            if nrx == nbx and nry == nby:
                if rcnt > bcnt:
                    nrx -= dr[i]
                    nry -= dc[i]
                else:
                    nbx -= dr[i]
                    nby -= dc[i]
            if not visited[nrx][nry][nbx][nby]:
                q.append([nrx, nry, nbx, nby, depth + 1])
    print('-1')


N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
visited = [[[[0] * M for i in range(N)] for j in range(M)] for k in range(N)]

point = [1] * 5
for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
            point[0], point[1] = i, j
        if board[i][j] == 'B':
            point[2], point[3] = i, j

bfs(point)
