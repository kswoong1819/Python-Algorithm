from collections import deque

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


def b_fire():  # 불채우는거

    while fq:
        r, c, cnt = fq.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < 0 or nr >= h or nc < 0 or nc >= w:
                continue
            if (Map[nr][nc] == '@' or Map[nr][nc] == '.') and fire_visited[nr][nc] == 0:
                fire_visited[nr][nc] = 1
                fire_cnt[nr][nc] = min(fire_cnt[nr][nc], cnt + 1)
                fq.append((nr, nc, cnt + 1))


def bfs(fire_cnt):

    while q:
        r, c, cnt = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < 0 or nr >= h or nc < 0 or nc >= w:
                print(cnt + 1)
                return
            if Map[nr][nc] == '.' and fire_cnt[nr][nc] > cnt + 1:
                if visited[nr][nc] == 0:
                    visited[nr][nc] = 1
                    q.append((nr, nc, cnt + 1))

    print("IMPOSSIBLE")


T = int(input())
for tc in range(T):

    w, h = map(int, input().split())

    Map = [list(input()) for _ in range(h)]
    visited = [[0] * w for _ in range(h)]
    fire_cnt = [[float('inf')] * w for _ in range(h)]
    fire_visited = [[0] * w for _ in range(h)]

    fq, q = deque(), deque()

    for i in range(w):
        for j in range(h):
            if Map[j][i] == '*':
                fq.append((j, i, 0))

            if Map[j][i] == '@':
                q.append((j, i, 0))
    b_fire()
    bfs(fire_cnt)