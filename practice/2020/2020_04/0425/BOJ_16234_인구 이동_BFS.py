import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def check(st):
    q = deque()
    q.append(st)
    m_country = [[st[0], st[1]]]
    population = country[st[0]][st[1]]
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0:
                if L <= abs(country[nr][nc] - country[r][c]) <= R:
                    visited[nr][nc] = 1
                    population += country[nr][nc]
                    m_country.append([nr, nc])
                    q.append([nr, nc])
    return m_country, population


def move(arr, person):
    cnt = 0
    avg = person // len(arr)
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
                m_country, cur = check([i, j])
                if len(m_country) > 1:
                    cnt += move(m_country, cur)
                else:
                    visited[i][j] = 0
    if cnt == 0:
        break
    ans += 1

print(ans)
