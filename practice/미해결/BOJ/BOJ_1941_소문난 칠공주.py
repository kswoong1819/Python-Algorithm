import sys

sys.stdin = open('input.txt')

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def go(k, r, c, current):
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < 5 and 0 <= nc < 5:
            next_str = current + arr[nr][nc]
            if k == 6:
                result.add(next_str)
            else:
                go(k + 1, nr, nc, next_str)


arr = [list(input()) for _ in range(5)]

result = set()
for i in range(5):
    for j in range(5):
        go(1, i, j, arr[i][j])

print(result)