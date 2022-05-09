import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def init_hole():
    q = deque()
    q.append((0, 0))
    visited = []
    ans = 0
    nq = []
    cnt_li = []
    while q:
        cnt = 0
        r, c = q.popleft()
        visited.append((r, c))
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M and (nr, nc) not in visited:
                if cheese[nr][nc] == 1:
                    cheese[nr][nc] = 2
                    nq.append((nr, nc))
                if cheese[nr][nc] == 0:
                    cheese[nr][nc] = -1
                    q.append((nr, nc))
        if len(q) == 0 and len(nq) != 0:
            ans += 1
            for x, y in nq:
                cnt += 1
                cheese[x][y] = 0
            cnt_li.append(cnt)
            q += nq
            nq = []
            visited = []
    return ans, cnt_li[-1]


N, M = map(int, input().split())
cheese = [list(map(int, input().split())) for _ in range(N)]

ans = init_hole()

for i in range(2):
    print(ans[i])

