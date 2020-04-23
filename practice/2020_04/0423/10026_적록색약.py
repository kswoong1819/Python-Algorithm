import sys

sys.stdin = open('input.txt')

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]


def change(st, type, visited):
    q = [st]
    while q:
        r, c = q.pop()
        visited[r][c] = 1
        color = painting[r][c]
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0:
                nxt_color = painting[nr][nc]
                if color == nxt_color:
                    q.append([nr, nc])
                if type == 1 and (color == 'R' or color == 'G') and (nxt_color == 'R' or nxt_color == 'G'):
                    q.append([nr, nc])


N = int(input())
painting = [list(input()) for _ in range(N)]
cnt, cnt_2 = 0, 0

visited = [[0] * N for _ in range(N)]
visited_2 = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            cnt_2 += 1
            change([i, j], 1, visited)
        if visited_2[i][j] == 0:
            cnt += 1
            change([i, j], 0, visited_2)

print(cnt, cnt_2)
