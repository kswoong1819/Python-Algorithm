import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline
from copy import deepcopy

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def find(map, cctv, cnt_zero, idx):
    global ans
    if idx == len(cctv):
        ans = min(ans, cnt_zero)
        return
    r, c, num = cctv[idx]
    if num == 1:
        for i in range(4):
            nxt_map, cnt = area(map, r, c, [i])
            find(nxt_map, cctv, cnt_zero - cnt, idx + 1)
    if num == 2:
        way = [[0, 2], [1, 3]]
        for i in way:
            nxt_map, cnt = area(map, r, c, i)
            find(nxt_map, cctv, cnt_zero - cnt, idx + 1)
    if num == 3:
        way = [[0, 1], [1, 2], [2, 3], [3, 0]]
        for i in way:
            nxt_map, cnt = area(map, r, c, i)
            find(nxt_map, cctv, cnt_zero - cnt, idx + 1)
    if num == 4:
        way = [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]]
        for i in way:
            nxt_map, cnt = area(map, r, c, i)
            find(nxt_map, cctv, cnt_zero - cnt, idx + 1)
    if num == 5:
        way = [0, 1, 2, 3]
        nxt_map, cnt = area(map, r, c, way)
        find(nxt_map, cctv, cnt_zero - cnt, idx + 1)


def area(maps, r, c, dir):
    map = deepcopy(maps)
    cnt = 0
    for i in dir:
        nr, nc = r, c
        while 1:
            nr += dr[i]
            nc += dc[i]
            if 0 > nr or nr >= N or 0 > nc or nc >= M:
                break
            if map[nr][nc] == 6:
                break
            if map[nr][nc] == 0:
                map[nr][nc] = '#'
                cnt += 1
    return map, cnt


N, M = map(int, input().split())
office = [list(map(int, input().split())) for _ in range(N)]

cnt_zero = 0
camera = []
for i in range(N):
    for j in range(M):
        if office[i][j] == 0:
            cnt_zero += 1
        if office[i][j] != 0 and office[i][j] != 6:
            camera.append([i, j, office[i][j]])

ans = cnt_zero
find(office, camera, cnt_zero, 0)
print(ans)
