import sys

sys.stdin = open('input.txt')
from collections import deque

dr_horse = [-1, -2, -2, -1, 1, 2, 2, 1]
dc_horse = [-2, -1, 1, 2, 2, 1, -1, -2]

dr_monkey = [0, 1, 0, -1]
dc_monkey = [1, 0, -1, 0]


def bfs():
    q = deque([[0, 0, 0]])
    while q:
        r, c, z = q.popleft()
        if r == H - 1 and c == W - 1:
            print(visited[r][c][z] - 1)
            return False

        if z < K:
            for i in range(8):
                nr = r + dr_horse[i]
                nc = c + dc_horse[i]
                if 0 <= nr < H and 0 <= nc < W:
                    if arr[nr][nc] == 0 and visited[nr][nc][z + 1] == 0:
                        visited[nr][nc][z + 1] = visited[r][c][z] + 1
                        q.append([nr, nc, z + 1])

        for i in range(4):
            nr = r + dr_monkey[i]
            nc = c + dc_monkey[i]
            if 0 <= nr < H and 0 <= nc < W:
                if arr[nr][nc] == 0 and visited[nr][nc][z] == 0:
                    visited[nr][nc][z] = visited[r][c][z] + 1
                    q.append([nr, nc, z])
    return True


K = int(input())
W, H = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(H)]
visited = [[[0] * (K + 1) for _ in range(W)] for _ in range(H)]
visited[0][0][0] = 1
if bfs():
    print('-1')
