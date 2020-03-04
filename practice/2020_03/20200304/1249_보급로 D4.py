import sys

sys.stdin = open('input.txt')

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def go(start, end):
    q = [start]
    while q:
        tmp = q.pop(0)
        r, c = tmp
        if tmp == end:
            continue
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                if check[nr][nc] == -1 or check[r][c] + arr[nr][nc] < check[nr][nc]:
                    check[nr][nc] = check[r][c] + arr[nr][nc]
                    q.append((nr, nc))
    return check[N-1][N-1]

T = int(input())

for t in range(T):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    check = [[-1] * N for _ in range(N)]
    check[0][0] = 0
    tmp = go((0, 0), (N-1, N-1))
    print('#{} {}'.format(t+1, tmp))
