import sys
sys.stdin = open('input.txt')

dr = [0, 0, 0, 1, 1]
dc = [0, 0, 1, 1, 0]

pipe = [[], [], [2, 3], [2, 3, 4], [3, 4]]

def bfs(st, ed):
    global cnt
    q = [st]
    if room[N-1][N-1] == 1:
        return
    while q:
        r, c = q.pop()
        for i in pipe[room[r][c]]:
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                if i == 3:
                    if room[nr-1][nc] == 1 or room[nr][nc-1] == 1:
                        continue
                if room[nr][nc] != 1:
                    room[nr][nc] = i
                    if (nr, nc) == ed:
                        cnt += 1
                        continue
                    q.append((nr, nc))

N = int(input())
room = [list(map(int, input().split())) for _ in range(N)]
room[0][1] = 2

cnt = 0
bfs((0, 1), (N-1, N-1))
print(cnt)