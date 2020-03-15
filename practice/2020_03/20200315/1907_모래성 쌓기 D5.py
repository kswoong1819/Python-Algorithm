import sys

sys.stdin = open('input.txt')

dr = [0, 1, 1, 1, 0, -1, -1, -1]
dc = [1, 1, 0, -1, -1, -1, 0, 1]


def makearr():
    q = []
    for r in range(H):
        for c in range(W):
            if castle[r][c] != '.':
                for j in range(8):
                    nr = r + dr[j]
                    nc = c + dc[j]
                    if castle[nr][nc] == '.':
                        castle[r][c] -= 1
                if castle[r][c] <= 0:
                    q.append([r, c])
    return q


def wave(st):
    ans = 0
    q = st
    nq = []
    while q:
        r, c = q.pop()
        castle[r][c] = '.'
        for j in range(8):
            nr = r + dr[j]
            nc = c + dc[j]
            if castle[nr][nc] != '.':
                castle[nr][nc] -= 1
                if castle[nr][nc] <= 0 and [nr, nc] not in nq and [nr, nc] not in q:
                    nq.append([nr, nc])
        if len(q) == 0:
            q = nq
            nq = []
            ans += 1
    return ans


T = int(input())

for t in range(T):
    H, W = map(int, input().split())
    castle = [[int(i) if i != '.' else i for i in input()] for _ in range(H)]

    q = makearr()

    print('#{} {}'.format(t + 1, wave(q)))
