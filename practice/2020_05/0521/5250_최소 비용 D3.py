import sys

sys.stdin = open('input.txt')

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def Dijkstra(my_map):
    key = [[float('inf')] * N for _ in range(N)]
    confirm = [[False] * N for _ in range(N)]
    key[0][0] = 0
    check = set()
    check.add((0, 0))
    while True:
        min_key = float('inf')
        for r, c in check:
            if key[r][c] < min_key and not confirm[r][c]:
                min_key = key[r][c]
                y, x = r, c

        confirm[y][x] = True
        check.remove((y, x))
        if y == x == N - 1:
            return key[y][x]

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not confirm[ny][nx]:
                if my_map[y][x] < my_map[ny][nx]:
                    fuel = key[y][x] + my_map[ny][nx] - my_map[y][x] + 1
                else:
                    fuel = key[y][x] + 1
                if fuel < key[ny][nx]:
                    key[ny][nx] = fuel
                    check.add((ny, nx))


T = int(input())
for test_case in range(1, 1 + T):
    N = int(input())
    my_map = [list(map(int, input().split())) for _ in range(N)]

    print('#{} {}'.format(test_case, Dijkstra(my_map)))
