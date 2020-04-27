import sys

sys.stdin = open('input.txt')
sys.setrecursionlimit(100000)
input = sys.stdin.readline

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def check(r, c, visit, cur):
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr < 0 or nr >= N or nc < 0 or nc >= N:
            continue
        if visited[nr][nc] == 1:
            continue
        if L <= abs(country[nr][nc] - country[r][c]) <= R:
            visited[nr][nc] = 1
            visit.append([nr, nc])
            cur.append(country[nr][nc])
            check(nr, nc, visit, cur)
    return visit, cur


def move(arr, person):
    cnt = 0
    avg = sum(person) // len(arr)
    for i in arr:
        if country[i[0]][i[1]] != avg:
            cnt += 1
            country[i[0]][i[1]] = avg
    return cnt


N, L, R = map(int, input().split())
country = [list(map(int, input().split())) for _ in range(N)]

flag = True
ans = 0
while 1:
    cnt = 0
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                visited[i][j] = 1
                m_country, cur = check(i, j, [[i, j]], [country[i][j]])
                if len(m_country) > 1:
                    cnt += move(m_country, cur)
                else:
                    visited[i][j] = 0
    if cnt == 0:
        break
    ans += 1

print(ans)
