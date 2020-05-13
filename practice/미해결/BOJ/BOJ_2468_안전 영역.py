import sys

sys.stdin = open('../../2020_05/0507/input.txt')

input = sys.stdin.readline
from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def find(n):
    cnt = 0
    visited = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if area[r][c] > n and visited[r][c] == 0:
                cnt += 1
                visited[r][c] = 1
                q = deque()
                q.append([r, c])
                while q:
                    r, c = q.popleft()
                    for i in range(4):
                        nr = r + dr[i]
                        nc = c + dc[i]
                        if 0 <= nr < N and 0 <= nc < N:
                            if area[nr][nc] > n and visited[nr][nc] == 0:
                                visited[nr][nc] = 1
                                q.append([nr, nc])
    return cnt


N = int(input())
area = [list(map(int, input().split())) for _ in range(N)]

water = 0
ans = [0, 0]
while ans[-2] <= ans[-1] and water < 101:
    ans.append(find(water))
    water += 1

print(max(ans))
