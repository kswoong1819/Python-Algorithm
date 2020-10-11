import sys

sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, 1 + T):
    N, M = map(int, input().split())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    houses = []
    for r in range(N):
        for c in range(N):
            if MAP[r][c]:
                houses.append((r, c))
    result = 1
    for K in range(2, N + 2):
        for r in range(N):
            for c in range(N):
                cnt = 0
                for y, x in houses:
                    if abs(r - y) + abs(c - x) < K:
                        cnt += 1
                if cnt > result and cnt * M >= K**2 + (K-1)**2:
                    result = cnt

    print('#{} {}'.format(test_case, result))
