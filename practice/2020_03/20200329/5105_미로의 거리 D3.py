import sys

sys.stdin = open('input.txt')

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def bfs(st):
    q = [st]
    ans = float('inf')
    while q:
        r, c, cnt = q.pop(0)
        maze[r][c] = 1
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                if maze[nr][nc] == 0:
                    q.append((nr, nc, cnt+1))
                if maze[nr][nc] == 3:
                    ans = min(ans, cnt)
    return ans

T = int(input())

for t in range(T):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                ans = bfs((i, j, 0))
                break

    print('#{} {}'.format(t+1, 0 if ans == float('inf') else ans))
