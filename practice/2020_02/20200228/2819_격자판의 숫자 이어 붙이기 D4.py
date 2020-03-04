import sys

sys.stdin = open('../../미해결/BOJ/input.txt')

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def go(k, r, c, current):
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < 4 and 0 <= nc < 4:
            next_num = current + str(arr[nr][nc])
            if k == 6:
                result.add(next_num)
            else:
                go(k + 1, nr, nc, next_num)

T = int(input())

for t in range(T):
    arr = [list(map(int, input().split())) for _ in range(4)]

    result = set()

    for i in range(4):
        for j in range(4):
            go(1, i, j, str(arr[i][j]))

    print('#{} {}'.format(t+1, len(result)))
