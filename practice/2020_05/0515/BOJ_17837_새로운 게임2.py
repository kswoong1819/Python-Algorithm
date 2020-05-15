import sys

sys.stdin = open('input.txt')

dr = [0, 0, 0, -1, 1]
dc = [0, 1, -1, 0, 0]


def move(st):
    global flag
    k, r, c, d = st
    chess_set = []
    for i, key in enumerate(chess_position[r][c]):
        if key == k:
            chess_set.extend(chess_position[r][c][i:])
            chess_position[r][c] = chess_position[r][c][:i]
            break

    nr = r + dr[d]
    nc = c + dc[d]
    if nr < 0 or nr >= N or nc < 0 or nc >= N or chess_board[nr][nc] == 2:
        nr = r - dr[d]
        nc = c - dc[d]
        if d % 2:
            d += 1
        else:
            d -= 1
        chess[k][3] = d
        if nr < 0 or nr >= N or nc < 0 or nc >= N or chess_board[nr][nc] == 2:
            nr, nc = r, c
            for i in chess_set:
                chess[i][:3] = [i, nr, nc]
            chess_position[r][c].extend(chess_set)
        else:
            for i in chess_set:
                chess[i][:3] = [i, nr, nc]
            if chess_board[nr][nc] == 1:
                chess_set.reverse()
            chess_position[nr][nc].extend(chess_set)

    elif chess_board[nr][nc] == 0:
        for i in chess_set:
            chess[i][:3] = [i, nr, nc]
        chess_position[nr][nc].extend(chess_set)

    elif chess_board[nr][nc] == 1:
        for i in chess_set:
            chess[i][:3] = [i, nr, nc]
        chess_set.reverse()
        chess_position[nr][nc].extend(chess_set)

    if len(chess_position[nr][nc]) >= 4:
        flag = False
        return True


N, K = map(int, input().split())
chess_board = [list(map(int, input().split())) for _ in range(N)]
chess = [[0]]
chess_position = [[[] for a in range(N)] for b in range(N)]
for k in range(1, K + 1):
    y, x, d = map(int, input().split())
    chess.append([k, y - 1, x - 1, d])
    chess_position[y - 1][x - 1].append(k)

cnt = 0
flag = True
while cnt < 1000 and flag:
    cnt += 1
    for i in range(1, K + 1):
        if move(chess[i]):
            break

if cnt == 1000:
    print('-1')
else:
    print(cnt)
