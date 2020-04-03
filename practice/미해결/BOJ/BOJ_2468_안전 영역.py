import sys
sys.stdin = open('../../2020_04/0403/input.txt')

input = sys.stdin.readline
from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def find():
    k = 0
    ans = 0
    while 1:
        cnt_zero = 0
        for i in range(N):
            for j in range(N):
                if area[i][j] == 0:
                    cnt_zero += 1
                if area[i][j] == k:
                    area[i][j] = 0
        if cnt_zero == N * N:
            break
        visited = [[0] * N for _ in range(N)]
        cnt = 0
        for r in range(N):
            for c in range(N):
                if area[r][c] != 0 and visited[r][c] == 0:
                    cnt += 1
                    q = deque()
                    q.append([r, c])
                    while q:
                        r, c = q.popleft()
                        visited[r][c] = 1
                        for i in range(4):
                            nr = r + dr[i]
                            nc = c + dc[i]
                            if 0 <= nr < N and 0 <= nc < N:
                                if area[nr][nc] != 0 and visited[nr][nc] == 0:
                                    visited[nr][nc] = 1
                                    q.append([nr, nc])
        ans = max(ans, cnt)
        k += 1
    return ans

N = int(input())
area = [list(map(int, input().split())) for _ in range(N)]

print(find())
