import sys

sys.stdin = open('input.txt')

from collections import deque

dr = [0, -1, 1, 0, 0]
dc = [0, 0, 0, -1, 1]


def move():
    matrix2 = [[1] * N] + [[1] + [0] * (N - 2) + [1] for _ in range(N - 2)] + [[1] * N]
    microbe2 = deque()
    overlap = {}
    while microbe:
        r, c = microbe.popleft()
        n, d = matrix[r][c]
        nr = r + dr[d]
        nc = c + dc[d]
        if matrix2[nr][nc] == 1:
            n //= 2
            if n == 0:
                continue
            if d % 2:
                d += 1
            else:
                d -= 1
            matrix2[nr][nc] = [n, d]
            microbe2.append([nr, nc])
        elif matrix2[nr][nc] == 0:
            matrix2[nr][nc] = [n, d]
            microbe2.append([nr, nc])
        else:
            if (nr, nc) not in overlap:
                overlap[nr, nc] = [[n, d]]
            else:
                overlap[nr, nc] += [[n, d]]

    for over_r, over_c in overlap:
        n1, d1 = matrix2[over_r][over_c]
        fi_n, fi_d = n1, d1
        for n2, d2 in overlap[over_r, over_c]:
            if n1 < n2:
                n1 = n2
                fi_d = d2
            fi_n += n2
        matrix2[over_r][over_c] = [fi_n, fi_d]

    return microbe2, matrix2


T = int(input())
for t in range(T):
    N, M, K = map(int, input().split())
    matrix = [[1] * N] + [[1] + [0] * (N - 2) + [1] for _ in range(N - 2)] + [[1] * N]
    microbe = deque()
    for _ in range(K):
        r, c, n, d = list(map(int, input().split()))
        matrix[r][c] = [n, d]
        microbe.append([r, c])

    for m in range(M):
        microbe, matrix = move()

    result = 0
    for r, c in microbe:
        result += matrix[r][c][0]

    print('#{} {}'.format(t + 1, result))
