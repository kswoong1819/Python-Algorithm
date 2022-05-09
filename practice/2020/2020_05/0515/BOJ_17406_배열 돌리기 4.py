import sys

sys.stdin = open('input.txt')
import copy

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def go(k, arr):
    global ans
    if k == K:
        for r, c, s in A:
            arr = rotation(r - s - 1, c - s - 1, r + s - 1, c + s - 1, arr)
        ans = min(ans, find(arr))
        return
    for i in range(K):
        if visited[i]:
            continue
        visited[i] = 1
        A.append(check[i])
        go(k + 1, arr)
        A.pop()
        visited[i] = 0


def rotation(r1, c1, r2, c2, arr):
    n_arr = copy.deepcopy(arr)
    R = (r1 + r2) // 2
    C = (c1 + c2) // 2
    while 1:
        d = 0
        nr = r1
        nc = c1
        while d < 4:
            tmp = arr[nr][nc]
            nr += dr[d]
            nc += dc[d]
            if nr < r1 or nr > r2 or nc < c1 or nc > c2:
                nr -= dr[d]
                nc -= dc[d]
                d += 1
                continue
            n_arr[nr][nc] = tmp
            if nr == r1 and nc == c1:
                break
        if R > r1 + 1 and C > c1 + 1:
            r1, c1 = r1 + 1, c1 + 1
            r2, c2 = r2 - 1, c2 - 1
        else:
            break
    return n_arr


def find(arr):
    tmp_min = float('inf')
    for i in range(N):
        tmp_min = min(tmp_min, sum(arr[i]))
    return tmp_min


N, M, K = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
check = []
for k in range(K):
    r, c, s = map(int, input().split())
    check.append([r, c, s])

ans = float('inf')
A = []
visited = [0] * K
go(0, matrix)

print(ans)
