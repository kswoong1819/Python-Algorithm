import sys

sys.stdin = open('input.txt')
from collections import deque
input = sys.stdin.readline

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def melt(st):
    q = deque()
    melting_q = deque()
    q.append(st)
    while q:
        r, c = q.popleft()
        cnt = 0
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < 0 or nr >= N or nc < 0 or nc >= M or visited[nr][nc] == 1:
                continue
            if ice[nr][nc] > 0:
                visited[nr][nc] = 1
                q.append([nr, nc])
            else:
                cnt += 1
        if cnt:
            melting_q.append([r, c, cnt])
    return melting_q


N, M = map(int, input().split())
ice = [list(map(int, input().split())) for _ in range(N)]

ans = -1
flag = True
while flag:
    ans += 1
    area = 0
    visited = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if area >= 2:
                flag = False
                break
            if ice[i][j] > 0 and visited[i][j] == 0:
                visited[i][j] = 1
                area += 1
                melting_q = melt([i, j])
                for x, y, cnt in melting_q:
                    ice[x][y] -= cnt
        if flag == False:
            break
    if area == 0:
        ans = 0
        break

print(ans)
