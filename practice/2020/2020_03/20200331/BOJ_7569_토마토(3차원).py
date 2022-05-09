import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque

dh = [-1, 1, 0, 0, 0, 0]
dr = [0, 0, 0, 1, 0, -1]
dc = [0, 0, 1, 0, -1, 0]


def bfs(st):
    global cnt_zero
    q = deque()
    q += st
    nq = deque()
    ans = -1
    while q:
        h, r, c = q.popleft()
        for i in range(6):
            nh = h + dh[i]
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nh < H and 0 <= nr < N and 0 <= nc < M:
                if tomato[nh][nr][nc] == 0:
                    tomato[nh][nr][nc] = 1
                    cnt_zero -= 1
                    nq.append((nh, nr, nc))
        if len(q) == 0:
            q = nq
            nq = deque()
            ans += 1
    return ans


M, N, H = map(int, input().split())
tomato = [[list(map(int, input().split())) for r in range(N)] for h in range(H)]

cnt_zero = 0
li_one = []
for i in range(H):
    for j in range(N):
        for z in range(M):
            n = tomato[i][j][z]
            if n == 0:
                cnt_zero += 1
            if n == 1:
                li_one.append((i, j, z))

result = bfs(li_one)
if cnt_zero > 0:
    print('-1')
else:
    print(result)
