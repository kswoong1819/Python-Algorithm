import sys
sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline
from collections import deque

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]


def bfs(start):
    global cnt_zero
    q = deque()
    q += start
    nq = deque()
    ans = -1
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M:
                if box[nr][nc] == 0:
                    box[nr][nc] = 1
                    cnt_zero -= 1
                    nq.append((nr, nc))
        if len(q) == 0:
            q = nq
            nq = deque()
            ans += 1
    return ans


M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]

cnt_zero = 0
li_one = []
for i in range(N):
    for j in range(M):
        n = box[i][j]
        if n == 1:
            li_one.append((i, j))
        elif n == 0:
            cnt_zero += 1

result = bfs(li_one)

if cnt_zero > 0:
    print('-1')
else:
    print(result)
