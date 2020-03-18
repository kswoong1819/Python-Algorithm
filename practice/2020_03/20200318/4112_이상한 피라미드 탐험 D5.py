import sys

sys.stdin = open('input.txt')


def find_line(X):
    N = 1
    ls = [1]
    while X >= ls[-1]:
        tmp = ls[N - 1] + N
        ls.append(tmp)
        N += 1
    return [ls[-2], N - 1]


dr = [0, 1, 1, 0]
dc = [1, 1, 0, -1]


def bfs(s, e):
    q = [s]
    visited = []
    ans = 0
    while q:
        n, cnt = q.pop(0)
        visited.append(n)
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr <


T = int(input())

for t in range(T):
    a, b = map(int, input().split())
    if a > b:
        a, b = b, a

    st_idx = find_line(a)
    ed_idx = find_line(b)

    st = (0, a - st_idx[0])
    ed = (ed_idx[1] - ed_idx[1], b - ed_idx[0])

    arr = []
    while st_idx[1] <= ed_idx[1]:
        arr.append([i for i in range(st_idx[0], st_idx[0] + st_idx[1])])
        st_idx[0] += st_idx[1]
        st_idx[1] += 1

    bfs((st, 0), ed)
