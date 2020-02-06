import sys
sys.stdin = open('input.txt', 'r')

dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    pan = [[0] * (N + 1) for _ in range(N + 1)]
    mid = N // 2
    pan[mid][mid] = pan[mid + 1][mid + 1] = 2
    pan[mid][mid + 1] = pan[mid + 1][mid] = 1

    for _ in range(M):
        x, y, dol = map(int, input().split())
        pan[x][y] = dol
        for i in range(8):
            attack = False
            tx, ty = x + dx[i], y + dy[i]
            while 1 <= tx <= N and 1 <= ty <= N:
                if pan[tx][ty] == 0: break
                if pan[tx][ty] == dol:
                    attack = True;
                    break
                tx, ty = tx + dx[i], ty + dy[i]

            if attack:
                tx, ty = tx - dx[i], ty - dy[i]
                while tx != x or ty != y:
                    pan[tx][ty] = dol
                    tx, ty = tx - dx[i], ty - dy[i]

    B = W = 0
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if pan[i][j] == 1:
                B += 1
            elif pan[i][j] == 2:
                W += 1

    print('#{} {} {}'.format(tc, B, W))