from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def solution(v):
    answer = [0] * 3
    L = len(v)
    for i in range(L):
        for j in range(L):
            if v[i][j] != -1:
                n = v[i][j]
                answer[n] += 1
                bfs(v, [i, j], n)
    return answer


def bfs(v, st, num):
    q = deque()
    q.append(st)
    while q:
        r, c = q.popleft()
        v[r][c] = -1
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < len(v) and 0 <= nc < len(v) and v[nr][nc] != -1:
                if num == v[nr][nc]:
                    q.append([nr, nc])


# v = [[0, 0, 1, 1], [1, 1, 1, 1], [2, 2, 2, 1], [0, 0, 0, 2]]
v = [[0, 0, 1], [2, 2, 1], [0, 0, 0]]
print(solution(v))
