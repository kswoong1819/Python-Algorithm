dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def solution(maze):
    global answer
    N = len(maze)
    dfs(0, 0, 0, 3, N, maze, 0)
    return answer


def dfs(r, c, d, d2, N, maze, cnt):
    global answer
    if r == N - 1 and c == N - 1:
        answer = cnt
        return
    nr = r + dr[d]
    nc = c + dc[d]
    if nr < 0 or nr >= N or nc < 0 or nc >= N or maze[nr][nc] == 1:
        d = (d + 1) % 4
        d2 = (d2 + 1) % 4
        dfs(r, c, d, d2, N, maze, cnt)
        if answer != 0:
            return
    nr2 = nr + dr[d2]
    nc2 = nc + dc[d2]
    if 0 <= nr2 < N and 0 <= nc2 < N:
        if maze[nr2][nc2] == 0:
            d = (d - 1) % 4
            d2 = (d2 - 1) % 4
    dfs(nr, nc, d, d2, N, maze, cnt + 1)


# maze = [[0, 1, 0, 1], [0, 1, 0, 0], [0, 0, 0, 0], [1, 0, 1, 0]]
# maze = [[0, 1, 0, 0, 0, 0], [0, 1, 0, 1, 1, 0], [0, 1, 0, 0, 1, 0], [0, 1, 1, 1, 1, 0], [0, 1, 0, 0, 0, 0],
#         [0, 0, 0, 1, 1, 0]]
# maze = [[0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0],
#         [1, 1, 1, 1, 1, 0]]
maze = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 0, 1, 1], [0, 0, 0, 0, 0, 0], [1, 0, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0],
        [1, 1, 0, 1, 1, 0]]
print(solution(maze))
