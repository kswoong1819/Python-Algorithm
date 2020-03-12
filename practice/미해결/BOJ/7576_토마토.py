import sys

sys.stdin = open('input.txt', 'r')

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]


def dfs(start):
    global cnt_zero
    q = start
    ans = 0
    while q:
        r, c, cnt = q.pop(0)
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M:
                if box[nr][nc] == 0:
                    box[nr][nc] = 1
                    cnt_zero -= 1
                    q.append((nr, nc, cnt + 1))
                    ans = max(ans, cnt + 1)
    return ans


M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]

cnt_zero = 0
li_one = []
for i in range(N):
    for j in range(M):
        n = box[i][j]
        if n == 1:
            li_one.append((i, j, 0))
        elif n == 0:
            cnt_zero += 1

result = dfs(li_one)

if cnt_zero > 0:
    print('-1')
else:
    print(result)
