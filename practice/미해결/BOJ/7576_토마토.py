import sys

sys.stdin = open('input.txt', 'r')
import copy

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]


def dfs(start):
    global result
    q = start
    while q:
        q_2 = copy.deepcopy(q)
        q = []
        result += 1
        while q_2:
            r, c = q_2.pop(0)
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < N and 0 <= nc < M:
                    if box[nr][nc] == 0:
                        box[nr][nc] = 1
                        q.append((nr, nc))


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

result = -1
dfs(li_one)

if cnt_zero > 0:
    print('-1')
else:
    print(result)
