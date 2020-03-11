import sys
sys.stdin = open('input.txt')

dr = [0, 0, 0, 1, 1]
dc = [0, 0, 1, 1, 0]

pipe = [[], [], [2, 3], [2, 3, 4], [3, 4]]

def bfs(st, ed):
    q = [st]
    while q:
        r, c = q.pop()
        for i in pipe[room[r-1][c-1]]:
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 < nr <= N and 0 < nc <= N:
                if i == 3:
                    if room[nr-2][nc-1] == 1 or room[nr-1][nc-2] == 1:
                        continue
                if room[nr-1][nc-1] != 1:
                    visited[nr][nc] += 1
                    room[nr-1][nc-1] = i
                    if (nr, nc) != ed:
                        q.append((nr, nc))
    return visited[N][N]

N = int(input())
room = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * (N+1) for _ in range(N+1)]
room[0][1] = visited[1][2] = 2

ans = bfs((1, 2), (N, N))
print(ans)