import sys

sys.stdin = open('input.txt')

dr = [0, -1, 1, 0, 0]
dc = [0, 0, 0, -1, 1]


def move_shark():
    global nq
    st = 1
    while st <= M:
        if alive_shark[st] == 0:
            st += 1
            continue
        flag = True
        for i in range(N):
            if not flag:
                break
            for j in range(N):
                if flag and matrix[i][j] == st:
                    flag = False
                    pri_dir = priority[st - 1][shark_dir[st] - 1]
                    tmp_move = []
                    check = True
                    for d in pri_dir:
                        nr = i + dr[d]
                        nc = j + dc[d]
                        if nr < 0 or nr >= N or nc < 0 or nc >= N:
                            continue
                        if smell[nr][nc] == [0, 0]:
                            matrix[i][j] = 0
                            shark_dir[st] = d
                            nq.append([nr, nc, st])
                            check = False
                            break
                        if not tmp_move and smell[nr][nc][0] == st:
                            tmp_move = [nr, nc, d]
                    if check:
                        nr, nc, d = tmp_move
                        matrix[i][j] = 0
                        shark_dir[st] = d
                        nq.append([nr, nc, st])
        st += 1


def decrease_smell():
    global q, nq
    i = 0
    while i < len(q):
        r, c, a = q[i]
        smell[r][c][1] -= 1
        if smell[r][c][1] <= 0:
            smell[r][c] = [0, 0]
            q.pop(i)
        else:
            i += 1
    for i in range(len(nq)):
        r, c, st = nq[i]
        if smell[r][c][1] == k:
            alive_shark[st] = 0
            nq[i] = []
        else:
            matrix[r][c] = st
            smell[r][c] = [st, k]
    for i in range(len(nq)):
        if nq[i] and nq[i] not in q:
            q.append(nq[i])
    nq = []


N, M, k = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
smell = [[[0, 0] for _ in range(N)] for _ in range(N)]
alive_shark = [i for i in range(M + 1)]
shark_dir = [0] + list(map(int, input().split()))
priority = [[list(map(int, input().split())) for _ in range(4)] for _ in range(M)]

ans = 0
q = []
nq = []

for i in range(N):
    for j in range(N):
        if matrix[i][j] != 0:
            smell[i][j] = [matrix[i][j], k]
            q.append([i, j, matrix[i][j]])

while ans <= 1000:
    if alive_shark.count(0) == M:
        break
    ans += 1
    move_shark()
    decrease_smell()

if ans > 1000:
    print('-1')
else:
    print(ans)
