import sys

sys.stdin = open('input.txt')

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

change = (
    (),
    (2, 0, 3, 1),
    (2, 3, 1, 0),
    (1, 3, 0, 2),
    (3, 2, 0, 1),
    (2, 3, 0, 1)
)


def dfs(r, c):
    result = 0
    for i in range(4):
        cnt = 0
        nr = r + dr[i]
        nc = c + dc[i]
        while 1:
            if matrix[nr][nc] == -1:
                break
            elif 0 < matrix[nr][nc] <= 5:
                i = change[matrix[nr][nc]][i]
                cnt += 1
            elif 6 <= matrix[nr][nc] <= 10:
                for hole in wormhole[matrix[nr][nc]]:
                    if hole != [nr, nc]:
                        nr, nc = hole
                        break
            nr += dr[i]
            nc += dc[i]

        if cnt > result:
            result = cnt

    return result


T = int(input())

for t in range(T):
    N = int(input())
    matrix = [[5] * (N + 2)] + [[5] + list(map(int, input().split())) + [5] for _ in range(N)] + [[5] * (N + 2)]

    wormhole = [[] for _ in range(11)]
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if 6 <= matrix[i][j] <= 10:
                wormhole[matrix[i][j]].append([i, j])

    max_ans = 0
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if matrix[i][j] == 0:
                matrix[i][j] = -1
                tmp = dfs(i, j)
                if max_ans < tmp:
                    max_ans = tmp
                matrix[i][j] = 0

    print('#{} {}'.format(t + 1, max_ans))
