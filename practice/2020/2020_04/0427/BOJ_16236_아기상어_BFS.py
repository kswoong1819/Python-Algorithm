import sys

sys.stdin = open('input.txt')
from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def eating(st):
    global baby
    q = deque()
    q.append(st)
    feed_r, feed_c = 20, 20
    min_cnt = 500
    while q:
        r, c, cnt = q.popleft()
        if min_cnt < cnt:
            continue
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0:
                if area[nr][nc] <= baby:
                    visited[nr][nc] = 1
                    q.append([nr, nc, cnt + 1])
                    if area[nr][nc] != 0 and area[nr][nc] != baby:
                        if min_cnt >= cnt + 1:
                            min_cnt = cnt + 1
                            if feed_r > nr:
                                feed_r = nr
                                feed_c = nc
                            elif feed_r == nr and feed_c > nc:
                                feed_c = nc
    if min_cnt == 500:
        return [0, 0], 0
    area[feed_r][feed_c] = 9
    return [feed_r, feed_c], min_cnt


N = int(input())
area = [list(map(int, input().split())) for _ in range(N)]

feed_cnt = 0
for i in range(N):
    for j in range(N):
        if area[i][j] == 9:
            shark_point = [i, j]
        if 1 <= area[i][j] <= 6:
            feed_cnt += 1

baby = 2
ans = 0
up = 0
while feed_cnt:
    x, y = shark_point[0], shark_point[1]
    visited = [[0] * N for _ in range(N)]
    visited[x][y] = 1
    shark_point, cnt = eating([x, y, 0])
    if cnt == 0:
        break
    up += 1
    feed_cnt -= 1
    if baby == up:
        baby += 1
        up = 0
    ans += cnt
    area[x][y] = 0

print(ans)
