import sys

sys.stdin = open('input.txt')

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def bfs(st):
    q = [st]
    visited = [st]
    while 1:
        if len(q) == 0:
            return 0
        tmp = q.pop(0)
        r, c = tmp
        if tmp not in visited:
            visited.append(tmp)
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < 16 and 0 <= nc < 16:
                if maze[nr][nc] == 0:
                    maze[nr][nc] = 2
                    q.append((nr, nc))
                if maze[nr][nc] == 3:
                    return 1


for t in range(10):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(16)]

    ans = bfs((1, 1))
    print('#{} {}'.format(N, ans))
