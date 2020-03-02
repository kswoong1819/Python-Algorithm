import sys
sys.stdin = open('../../2020_03/20200302/input.txt')

tunnel = {
    1: ((1, 0), (0, 1), (-1, 0), (0, -1)),
    2: ((1, 0), (-1, 0)),
    3: ((0, 1), (0, -1)),
    4: ((-1, 0), (0, 1)),
    5: ((1, 0), (0, 1)),
    6: ((1, 0), (0, -1)),
    7: ((-1, 0), (0, -1))
}




T = int(input())

for t in range(T):
    N, M, R, C, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

