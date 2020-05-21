import sys

sys.stdin = open('input.txt')
from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def find():
    check = 0
    visited = [[0] * 6 for _ in range(12)]
    for i in range(12):
        for j in range(6):
            if visited[i][j] == 0 and board[i][j] != '.':
                color = board[i][j]
                visited[i][j] = 1
                q = deque()
                nq = deque()
                q.append([i, j])
                nq.append([i, j])
                while q:
                    r, c = q.popleft()
                    for d in range(4):
                        nr = r + dr[d]
                        nc = c + dc[d]
                        if 0 <= nr < 12 and 0 <= nc < 6 and visited[nr][nc] == 0:
                            if color == board[nr][nc]:
                                visited[nr][nc] = 1
                                q.append([nr, nc])
                                nq.append([nr, nc])
                if len(nq) >= 4:
                    check += 1
                    for x, y in nq:
                        board[x][y] = '.'
    if check == 0:
        return False
    return True


def gravity():
    for i in range(10, -1, -1):
        for j in range(6):
            if board[i][j] != 0:
                color = board[i][j]
                nr = i
                while 1:
                    nr += dr[1]
                    if nr >= 12 or board[nr][j] != '.':
                        nr -= dr[1]
                        break
                board[i][j] = '.'
                board[nr][j] = color


board = [list(input()) for _ in range(12)]

ans = 0
while 1:
    flag = find()
    if not flag:
        break
    gravity()
    ans += 1

print(ans)
