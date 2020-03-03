import sys
sys.stdin = open('input.txt')

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

pipe = [[], [0, 1, 2, 3], [1, 3], [0, 2], [0, 3], [0, 1], [1, 2], [2, 3]]

def f(N, M, R, C, L):
    q = [(R, C)]
    v = [[0] * M for _ in range(N)]
    v[R][C] = 1
    pos = [0] * (L + 1)
    while q:
        i, j = q.pop(0)
        pos[v[i][j]] += 1
        if v[i][j] < L:
            for x in pipe[tunnel[i][j]]:
                ni = i + di[x]
                nj = j + dj[x]
                if 0 <= ni < N and 0 <= nj < M and tunnel[ni][nj] != 0 and v[ni][nj] == 0 and (x + 2) % 4 in pipe[tunnel[ni][nj]]:
                    v[ni][nj] = v[i][j] + 1
                    q.append((ni, nj))
    return sum(pos)


T = int(input())
for t in range(T):
    N, M, R, C, L = map(int, input().split())
    tunnel = [list(map(int, input().split())) for _ in range(N)]
    r = f(N, M, R, C, L)
    print('#{} {}'.format(t + 1, r))
